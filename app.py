import asyncio
import uuid
import os
import subprocess
import os
import pypandoc
import json

from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from utility import create_folder,deleteFolder,chat_with_gpt
from doc import extract_text_from_pdf,ocr_pdf
from prompts import resume_prompt




load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    print("Healthy Flask")
    return "Doc parser Flask Running!"


@app.route("/extract-content", methods=["POST"])
def extractcontentsFromDocs():
    unique_path = uuid.uuid4().hex
    output_path = os.path.abspath(f"temp/{unique_path}")

    try:
        # Ensure the temp folder exists
        create_folder(output_path)

        # Check if a file is in the request
        if "file" not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        # Save the uploaded file
        file_extension = file.filename.split('.')[-1].lower()
        document_path = os.path.join(output_path, f"document.{file_extension}")
        file.save(document_path)

        # Convert to PDF if necessary
        if file_extension == "pdf":
            pdf = document_path
        else:
            converted_path = os.path.join(output_path, "document.pdf")
            print("Converting to PDF")
            pypandoc.convert_file(document_path, "pdf", outputfile=converted_path)
            pdf = converted_path

        # Extract text from the PDF
        raw_text = extract_text_from_pdf(pdf)
        print(f"Text Extracted: {len(raw_text)} characters")

        # If no text extracted, use OCR as a fallback
        if len(raw_text) == 0:
            raw_text = ocr_pdf(pdf)

        if len(raw_text) == 0:
            return jsonify({"error": "Couldn't extract text"}), 500
        extracted_data = chat_with_gpt(system_prompt=resume_prompt,user_prompt=raw_text,model="gpt-4o-mini",max_tokens=350)
        return jsonify(extracted_data)

    except Exception as err:
        print("Error:", err)
        return jsonify({"error": "Something went wrong"}), 500

    finally:
        deleteFolder(output_path)


if __name__ == "__main__":
    port = 8080
    print(f"App running on port {port}")
    app.run(host="0.0.0.0", port=port, debug=True)