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

insights_prompt = """
You are an expert career analyst and mentor. Below is a JSON object containing a candidate's resume data and a job description for a position they want to apply to.

Your goal is to provide a thoughtful, human, and constructive evaluation of how well the candidate aligns with the role — not just pass/fail, but highlighting strengths, noting gaps, and offering a clear, actionable roadmap for improvement. Think of it as career coaching, not gatekeeping.

Based on the resume data and job description, respond in the following JSON format:
{
  "isEligible": boolean,
  "remarks": "string",
  "strengths": ["string"],
  "areasToImprove": ["string"],
  "missingRequirements": {
    "skills": ["string"],
    "degrees": ["string"],
    "experience": ["string"]
  },
  "expectedAveragePay": {
    "amount": "string",
    "country": "string (inferred from resume data, e.g., institution or company location)"
  },
  "roadmapToSuccess": [
    "string (specific step or recommendation to improve skills or experience)",
    "string",
    ...
  ]
}

Instructions:
- "isEligible": True if the candidate closely matches the job requirements; False if key elements are missing.
- "remarks": A warm, motivating summary of their current standing — praise their strong points, gently address gaps, and encourage growth.
- "strengths": List specific skills, experiences, or credentials that match the job description.
- "areasToImprove": Mention areas that can be improved to strengthen the candidate's profile.
- "missingRequirements": Include only requirements clearly missing from the resume.
- "expectedAveragePay": Estimate the candidate’s salary range based on their location, experience, and industry. In the "amount" field, use the most relevant currency symbol and formatting based on the **inferred country** from the resume (e.g., from address, past company locations, or institution names).
- "roadmapToSuccess": Provide clear, actionable steps the candidate can follow to become a stronger fit for the role.

Use a professional, kind, and encouraging tone — your goal is to help the candidate grow, feel inspired, and see a clear path forward in their career.

Only respond in the exact JSON format specified.
"""
