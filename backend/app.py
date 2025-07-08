from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz  # PyMuPDF
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "https://ai-job-assistant-mu.vercel.app"])


# Securely load the OpenRouter API key from environment
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def extract_text_from_pdf(file):
    try:
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text.strip()
    except Exception as e:
        return ""

@app.route("/generate-cover-letter", methods=["POST"])
def generate_cover_letter():
    job_description = request.form.get("job_description", "")
    resume_text = request.form.get("resume", "")
    file = request.files.get("resume_file")

    if file and file.filename.endswith(".pdf"):
        resume_text = extract_text_from_pdf(file)

    if not job_description or not resume_text:
        return jsonify({"error": "Job description and resume are required."}), 400

    prompt = f"""
You are an expert job coach.
Here is the job description:
{job_description}

Here is the applicant's resume or profile:
{resume_text}

Generate a tailored, professional cover letter aligned with the job description.
Use a confident, enthusiastic tone and focus on relevant skills.
"""

    try:
        response = client.chat.completions.create(
            model="mistralai/mixtral-8x7b-instruct",
            messages=[
                {"role": "system", "content": "You generate personalized cover letters."},
                {"role": "user", "content": prompt}
            ]
        )

        cover_letter = response.choices[0].message.content.strip()
        return jsonify({"cover_letter": cover_letter})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
