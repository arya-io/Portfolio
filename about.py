import streamlit as st
from PIL import Image

def display_about():
    st.title("About Me")
    st.write("---")

    st.header("Hello! I'm Arya")
    st.write("""
        Aspiring Data Scientist with a passion for AI. Ever since AI started emerging as a transformative technology, 
        I knew I wanted to be part of it. The power of AI to solve complex problems and drive innovation captured my interest, 
        and that’s why I chose to pursue a career in this exciting field.
    """)

    st.write("---")

    st.header("🔍 My Journey")
    st.write("""
        My journey began with a fascination for AI's potential. Over time, I’ve committed myself to continuous learning and 
        exploring the endless possibilities of **Generative AI** and **Data Science**. 
        These fields fuel my curiosity, and I thrive in environments that encourage teamwork and innovation.
    """)
    st.write("---")

    # Education Section
    st.header("🎓 Education")
    st.write("""
        I graduated from **G. H. Raisoni College of Engineering, Nagpur** with a **B.Tech Degree in Artificial Intelligence**. 
        During my studies, I co-authored two research papers:
    """)
    st.markdown("""
    1. **Traffic Sign Viewer** (Published in IJCRT).
    2. **Run Chase Prediction in IPL** (Published in IJSREM).
    """)

    st.write("""
        I also received a **copyright** from the **Government of India** for a poster on **Composite Material Property Prediction Using Machine Learning Algorithm**.
    """)
    st.write("---")

    # Internship Experience Section
    st.header("💼 Internship Experience")
    st.write("""
        I completed a **6-month internship** as a **Data Scientist and Social Media Manager** at **IPL Scoop**, 
        where I led a project on **Run Chase Prediction in IPL** and successfully grew the company's Twitter (X) followers from **48 to 1000+**.
    """)
    st.write("---")

    # Core Values and Beliefs Section
    st.header("🚀 What Drives Me")  # Subheading for core values
    st.success("""
        "Continuous learning, innovation, and teamwork are the cornerstones of my approach. Curiosity fuels my journey in AI and data-driven technologies."
    """)
    st.write("---")

    # Future Aspirations Section
    st.header("🌟 Future Aspirations")  # Subheading for future goals
    st.write("""
        My future goal is to contribute to innovative projects as a **Data Scientist**, **Data Engineer**, or **Generative AI Engineer**. 
        I aim to tackle real-world challenges and make a meaningful impact in AI and Data Science.
    """)  # Explain your career goals or aspirations
    st.write("---")

    # Hobbies and Interests
    st.header("🎯 Outside of Work")
    st.write("""
        When I'm not working, you can find me playing **Badminton**, going on **Trekking** adventures, 
        or enjoying a good book under the stars while **stargazing**.
    """)
    st.write("---")

    # Language Proficiency Section
    st.markdown("### 🌐 Language Proficiency")
    st.markdown("""
    - **English**: Fluent
    - **Hindi**: Fluent
    - **Marathi**: Native speaker
    - **Punjabi**: Basic (Beginner level)
    - **Japanese**: Basic (Beginner level)
    """)
