# Career Path Recommendation System

The Career Path Recommendation System is a web application built using Streamlit that helps users discover potential career paths based on their resumes. The application leverages resume parsing and a career recommendation model to provide tailored suggestions to users.

## Overview

This application has two main components:

1. **Client (Streamlit)**: A user interface that allows users to upload their resumes and view career path recommendations.
2. **Server (Flask API)**: Processes the uploaded resume, extracts relevant data, and generates career recommendations.

## Features

- **Resume Upload**: Users can upload their resumes in PDF format.
- **Resume Parsing**: The system extracts key information from the uploaded resume.
- **Career Path Recommendations**: The system generates personalized career paths based on the extracted resume data.

## Technologies Used

- **Python**: The main programming language.
- **Streamlit**: Used for building the web application's front end.
- **Flask**: Used for the server-side API.
- **resume-parser**: Library for extracting data from resumes.
- **dotenv**: Manages environment variables.
- **CareerPathRecommender**: A custom model that generates career recommendations.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- `pip` (Python package manager)

### Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/ResumeAnalyzer.git
cd ResumeAnalyzer
```
2. **Set Up the Server (Flask API)**

Navigate to the server folder and install the dependencies:

 ```bash
cd server
pip install -r requirements.txt
 ```

Start the Flask server:

```bash
python app.py
```
This will start the server on http://localhost:5000.


3. **Set Up the Client (Streamlit)**

Open a new terminal window, navigate to the client folder, and install the required dependencies:

 ```bash
cd ../client
pip install -r requirements.txt
```
Start the Streamlit app:

 ```bash
streamlit run app.py
```
This will start the client on http://localhost:8501.


### Environment Variables

Create a `.env` file in both the `server` and `client` folders to securely manage any sensitive information or configurations needed by your application.

### Usage

1. Visit `http://localhost:8501` to access the Streamlit web interface.
2. Upload your resume in PDF format.
3. View the recommended career paths based on your resume content.
