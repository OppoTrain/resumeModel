import streamlit as st
import os
from dotenv import load_dotenv
from resume_parser import parse_resume
from career_model import CareerPathRecommender

# Load environment variables
load_dotenv()

def main():
    st.title("Career Path Recommendation System")

    # File upload
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
    if uploaded_file is not None:
        resume_data = parse_resume(uploaded_file)
        recommender = CareerPathRecommender()
        career_paths = recommender.get_recommendations(resume_data)

        st.subheader("Recommended Career Paths:")
        
        # Display the formatted output
        if isinstance(career_paths, str):  # Ensure the return type is a string
            st.markdown(career_paths)
        else:
            st.write("No recommendations available.")

if __name__ == "__main__":
    main()
