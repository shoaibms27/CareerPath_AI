# career_advisor.py

import streamlit as st
import google.generativeai as genai

# Use API key from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def get_career_guidance(q1, q2, q3, q4, q5):
    prompt = f"""
    I am building a career guidance chatbot. A student has answered the following questions:

    1. Enjoyed subjects: {q1}
    2. Strengths or skills: {q2}
    3. Dream job/life: {q3}
    4. Preferred work type: {q4}
    5. Curious fields: {q5}

    Based on this, suggest 2-3 best-fit career options for them. 
    For each career, briefly explain why it suits the student and how they can start preparing for it.
    Be friendly and motivational in your tone.
    """

    response = model.generate_content(prompt)
    return response.text
