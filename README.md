# CareerPath AI – Smart Career Advisor for Students 🎓

## 📌 Project Overview
**CareerPath AI** is an intelligent career guidance chatbot built using **Google Gemini Pro** and **Streamlit**. It helps students navigate their career choices by analyzing their interests, skills, and aspirations. The app provides personalized career suggestions with actionable steps to guide students in making informed career decisions.

---

## 🔧 **Technologies Used**
- **Backend:** Google Gemini API
- **Frontend:** Streamlit
- **Environment:** Python, Google Cloud, Streamlit Cloud
- **Other Tools:** Git, GitHub, dotenv (for managing secrets)

---

## 🌟 **Key Features**
- **Interactive Q&A:** Students answer a few questions about their interests, strengths, and aspirations.
- **Personalized Career Recommendations:** Based on the input, the app suggests suitable career options.
- **Motivational Guidance:** Provides motivational advice to help students understand why the suggested careers align with their answers.
- **Easy-to-use Interface:** Clean and intuitive UI powered by Streamlit.

---

## 🧑‍💻 **How it Works**

1. The user answers a series of questions regarding their:
   - Interests in subjects
   - Strengths and skills
   - Desired career goals and work preferences
   - Curious fields or industries
2. The app processes this information using the **Google Gemini Pro API** to generate a personalized list of career suggestions.
3. The app displays the career options with detailed explanations about why they are a good fit for the student.
4. The student can use this guidance to make better career decisions.

---

## 🚀 **How to Run Locally**

### Prerequisites:
- Python 3.7 or above
- `pip` (Python package manager)

### Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/shoaibms27/CareerPath-AI.git
   cd CareerPath-AI

2. **Set up environment variables:**
   - Create a `.env` file in the root directory
   - Add your Google Gemini API key:
     ```bash
     GOOGLE_API_KEY=your_api_key_here
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run main.py
   ```

The app will open in your default web browser at `http://localhost:8501`

---

## 🔑 **Environment Variables**

The following environment variables are required:

| Variable | Description |
|----------|-------------|
| `GOOGLE_API_KEY` | Your Google Gemini API key |

---

## 🤝 **Contributing**

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

---

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 **Authors**

- Mohammed Shoeb - [GitHub](https://github.com/shoaibms27)

---

## 🙏 **Acknowledgments**

- Google for providing the Gemini Pro API
- Streamlit for their amazing framework
- All contributors who help improve this project

---

## 📞 **Support**

If you have any questions or run into issues, please open an issue in the GitHub repository.
