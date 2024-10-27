# app/main.py
import streamlit as st
from utils import extract_text_from_pdf,analyze_resume_with_llama3

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ("Home", "Upload Resume", "About"))

    if page == "Home":
        st.title("Welcome to the Resume Analyzer!")
        st.write("This application allows you to analyze your resume.")

    elif page == "Upload Resume":
        upload_resume()

    elif page == "About":
        st.title("About")
        st.write("This app analyzes resumes and provides career suggestions.")

def upload_resume():
    st.title("Resume Analyzer")
    
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

    if st.button("Analyze Resume"):
        if uploaded_file is not None:
            # Read the uploaded PDF file data
            file_data = uploaded_file.getvalue()

            # Extract text from the uploaded PDF
            resume_text = extract_text_from_pdf(file_data)

            # Analyze resume text
            career_suggestions = analyze_resume_with_llama3(resume_text)
            
            # Display the results
            st.success("Career Suggestions:")
            st.text(career_suggestions)
        else:
            st.warning("Please upload a PDF resume.")

if __name__ == "__main__":
    main()
