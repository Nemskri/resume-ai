resume_prompt = """
Below is data extracted from a resume, give output in this JSON format.
{
  "name": "string",
  "email": "string",
  "phone": "string",
  "summary": "string",
  "skills": ["string"],
  "experience": [
    {
      "title": "string",
      "company": "string",
      "period": "string",
      "description": "string"
    }
  ],
  "education": [
    {
      "degree": "string",
      "institution": "string",
      "year": "string"
    }
  ]
}
"""