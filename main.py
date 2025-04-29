# Import necessary module
import streamlit as st
from career_advisor import get_career_guidance

st.set_page_config(page_title="AI Career Guide", page_icon="🎓")
st.title("🎓Smart Creer Chatbot by Shoeb")

st.markdown("**Answer the following questions and let AI help you discover the best career path for you!**")

# Input form
q1 = st.text_input("1️⃣ What subjects or topics do you enjoy the most?")
q2 = st.text_input("2️⃣ What are your strengths or skills? (e.g., coding, communication, drawing)")
q3 = st.text_input("3️⃣ What is your dream job or what kind of life do you imagine?")
q4 = st.text_input("4️⃣ Do you prefer working with people, data, machines, or ideas?")
q5 = st.text_input("5️⃣ Any specific fields you're curious about? (Optional)")

if st.button("🎯 Get Career Suggestion"):
    if q1 and q2 and q3 and q4:
        with st.spinner("Thinking about your future..."):
            response = get_career_guidance(q1, q2, q3, q4, q5)
        st.success("✅ Career Suggestions Ready!")
        st.subheader("🔍 Personalized Career Recommendations:")
        st.write(response)
    else:
        st.warning("Please answer at least the first 4 questions.")

