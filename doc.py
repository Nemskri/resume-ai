import fitz  # PyMuPDF
import pytesseract

from io import BytesIO
from pdfminer.high_level import extract_text as pdf_extract_text
from PIL import Image


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf_bytes = f.read()

    text = pdf_extract_text(BytesIO(pdf_bytes))
    text = "\n".join(line.strip()
                     for line in text.splitlines() if line.strip())
    return text

def ocr_pdf(scanned_pdf):
    scanned_pdf = fitz.open(scanned_pdf)
    ocr_text = []
    for page_number in range(len(scanned_pdf)):
        page = scanned_pdf.load_page(page_number)
        pix = page.get_pixmap()
        img_data = pix.pil_tobytes("png")
        img = Image.open(BytesIO(img_data))
        text = pytesseract.image_to_string(img)
        ocr_text.append(text)
        return ocr_text
