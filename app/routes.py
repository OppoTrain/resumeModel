import os
from flask import Blueprint, request, jsonify
from .utils import extract_text_from_pdf, analyze_resume_with_llama3

main_bp = Blueprint('main', __name__)

@main_bp.route('/analyze_resume', methods=['POST'])
def analyze_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['resume']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Invalid file format. Only PDF files are allowed."}), 400

    file_path = os.path.join("uploads/", file.filename)
    file.save(file_path)
    
    resume_text = extract_text_from_pdf(file_path)
    
    try:
        career_suggestions = analyze_resume_with_llama3(resume_text)
        return jsonify({"career_suggestions": career_suggestions}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
