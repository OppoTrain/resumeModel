import os
import PyPDF2
from together import Together

api_key = os.getenv("TOGETHER_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set TOGETHER_API_KEY environment variable.")
client = Together(api_key=api_key)

# Function to extract text from uploaded PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def analyze_resume_with_llama3(resume_text):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
        messages=[
            {"role": "system", "content": "You are a career advisor."},
            {"role": "user", "content": (
                f"Analyze this resume and suggest up to three career paths. "
                f"For each career path, provide a brief description of relevant technologies, "
                f"tools, or skills commonly used in that field. The response should follow this format:\n\n"
                f"1. Career Field: Description of technologies, tools, or skills\n"
                f"2. Career Field: Description of technologies, tools, or skills\n"
                f"3. Career Field: Description of technologies, tools, or skills\n\n"
                f"Here is the resume: {resume_text}"
            )}
        ],
        max_tokens=500,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>", "<|eom_id|>"],
        stream=False
    )

    try:
        return response.choices[0].message.content
    except AttributeError:
        return "Unexpected response format"
