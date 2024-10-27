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
            # Retrieve and display the career suggestions from the FastAPI response
            career_suggestions = response.json().get("recommendations")
            
            # Ensure the recommendations are a string before displaying
            if isinstance(career_suggestions, str):
                st.success("Career Suggestions:")
                st.markdown(f'<div class="recommendation">{career_suggestions}</div>', unsafe_allow_html=True)
            else:
                st.write("No recommendations available.")
        else:
            # Display error message
            error_message = response.json().get('error', 'Unexpected error occurred')
            st.error(f"Error: {error_message}")
    else:
        st.warning("Please upload a PDF resume.")
