import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from resume_parser import parse_resume
from career_model import CareerPathRecommender

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend_career_paths():
    # Check if a file was uploaded
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    uploaded_file = request.files['resume']
    
    # Ensure the file is a PDF
    if uploaded_file.filename == '' or not uploaded_file.filename.endswith('.pdf'):
        return jsonify({'error': 'Invalid file type. Please upload a PDF.'}), 400

    # Parse the resume
    resume_data = parse_resume(uploaded_file)

    # Initialize the recommender
    recommender = CareerPathRecommender()

    # Get recommendations
    career_paths = recommender.get_recommendations(resume_data)

    # Check if recommendations are available
    if isinstance(career_paths, str):
        return jsonify({'recommendations': career_paths}), 200
    else:
        return jsonify({'error': 'No recommendations available.'}), 404

if __name__ == "__main__":
    app.run(debug=True)


# import streamlit as st
# import os
# from dotenv import load_dotenv
# from resume_parser import parse_resume
# from career_model import CareerPathRecommender

# # Load environment variables
# load_dotenv()

# def main():
#     st.title("Career Path Recommendation System")

#     # File upload
#     uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
#     if uploaded_file is not None:
#         resume_data = parse_resume(uploaded_file)
#         recommender = CareerPathRecommender()
#         career_paths = recommender.get_recommendations(resume_data)

#         st.subheader("Recommended Career Paths:")
        
#         # Display the formatted output
#         if isinstance(career_paths, str):  # Ensure the return type is a string
#             st.markdown(career_paths)
#         else:
#             st.write("No recommendations available.")

# if __name__ == "__main__":
#     main()
