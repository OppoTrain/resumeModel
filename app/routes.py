import os
from flask import Blueprint, request, jsonify
from .utils import extract_text_from_pdf, analyze_resume_with_llama3
from fastapi import APIRouter,UploadFile,File,HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post('/analyze_resume')
async def analyze_resume(file: UploadFile=File(...)):
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['resume']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if not file.filename.lower().endswith('.pdf'):
       raise HTTPException(status_code=400,detail="Invalid file format. Only PDF files are allowed.")

    file_path = os.path.join("uploads/", file.filename)
    with open(file_path,"wb") as buffer:
        buffer.write(await file.read())
    file.save(file_path)
    
    resume_text = extract_text_from_pdf(file_path)
    
    try:
        career_suggestions = analyze_resume_with_llama3(resume_text)
        return JSONResponse(content={"career_suggestions": career_suggestions}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))