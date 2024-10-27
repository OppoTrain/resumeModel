import streamlit as st
import requests

# Set the title of the Streamlit app
st.title("Resume Analyzer")

# File uploader for the PDF resume
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

# Button to analyze the resume
if st.button("Analyze Resume"):
    if uploaded_file is not None:
        # Send the uploaded file to your FastAPI endpoint
        files = {"resume": (uploaded_file.name, uploaded_file, "application/pdf")}
        response = requests.post("https://models-elrn.onrender.com/recommend", files=files)
        
        if response.status_code == 200:
            # Display the career suggestions returned from the FastAPI app
            career_suggestions = response.json().get("career_suggestions")
            st.success("Career Suggestions:")
            st.text(career_suggestions)
        else:
            # Display error message
            st.error(f"Error: {response.json().get('error')}")
    else:
        st.warning("Please upload a PDF resume.")
