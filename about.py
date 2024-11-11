import streamlit as st
from PIL import Image

def display_about():
    # Set page title and sidebar image
    st.title("About Me")  # Set the main title for the About page
    st.write("---")  # Draws a line to visually separate sections

    # Introduction Section with image
    # col1, col2 = st.columns([1, 2])  # Create two columns: col1 for the image, col2 for the text
    
    # with col1:
    #     # Load and display an image in the first column (replace with your own image)
    #     image = Image.open("Arya1.jpg")  # Load the image from the specified file path
    #     st.image(image, caption="Arya", use_column_width=True)  # Display the image with a caption

    # with col2:
    # Write a short introduction about yourself in the second column
    st.header("Hello! I'm Arya")  # Add a subheading for your name
     st.write("""
        Aspiring Data Scientist with a passion for AI. Ever since AI started emerging as a transformative technology, 
        I knew I wanted to be part of it. The power of AI to solve complex problems and drive innovation captured my interest, 
        and that’s why I chose to pursue a career in this exciting field.
    """)  # Provide an introduction paragraph

    st.write("---")  # Draw another line to separate the next section

    # Professional Journey Section with icons
    st.header("🔍 My Journey")  # Subheading for the journey section
    st.write("""
        My journey began with a fascination for AI's potential. Over time, I’ve committed myself to continuous learning and 
        exploring the endless possibilities of **Generative AI** and **Data Science**. 
        These fields fuel my curiosity, and I thrive in environments that encourage teamwork and innovation.
    """)  # Describe your career or learning journey so far
    st.write("---")

    # Education Section
    st.header("🎓 Education")  # Subheading for education
    st.write("""
        I graduated from **G. H. Raisoni College of Engineering, Nagpur** with a **B.Tech Degree in Artificial Intelligence**. 
        During my studies, I co-authored two research papers:
    """)  # Briefly explain your education background
    st.markdown("""
    1. **Traffic Sign Viewer** (Published in IJCRT).
    2. **Run Chase Prediction in IPL** (Published in IJSREM).
    """)  # List out your research papers

    st.write("""
        I also received a **copyright** from the **Government of India** for a poster on **Composite Material Property Prediction Using Machine Learning Algorithm**.
    """)  # Mention any significant achievements during your education
    st.write("---")

    # Internship Experience Section
    st.header("💼 Internship Experience")  # Subheading for internships
    st.write("""
        I completed a **6-month internship** as a **Data Scientist and Social Media Manager** at **IPL Scoop**, 
        where I led a project on **Run Chase Prediction in IPL** and successfully grew the company's Twitter (X) followers from **48 to 1000+**.
    """)  # Provide details about your internship experience
    st.write("---")

    # Core Values and Beliefs Section with a quote box
    st.header("🚀 What Drives Me")  # Subheading for core values
    st.success("""
        "Continuous learning, innovation, and teamwork are the cornerstones of my approach. Curiosity fuels my journey in AI and data-driven technologies."
    """)  # Display a motivational quote or statement about your professional values
    st.write("---")

    # Future Aspirations Section
    st.header("🌟 Future Aspirations")  # Subheading for future goals
    st.write("""
        My future goal is to contribute to innovative projects as a **Data Scientist**, **Data Engineer**, or **Generative AI Engineer**. 
        I aim to tackle real-world challenges and make a meaningful impact in AI and data science.
    """)  # Explain your career goals or aspirations
    st.write("---")

    # Hobbies and Interests Section with icons
    st.header("🎯 Outside of Work")  # Subheading for hobbies and interests
    st.write("""
        When I'm not working, you can find me playing **Badminton**, going on **Trekking** adventures, 
        or enjoying a good book under the stars while **stargazing**.
    """)  # Describe your hobbies and interests
    st.write("---")

    # Language Proficiency Section with emojis for a modern touch
    st.markdown("### 🌐 Language Proficiency")  # Subheading for language skills
    st.markdown("""
    - **English**: Fluent
    - **Hindi**: Fluent
    - **Marathi**: Native speaker
    - **Punjabi**: Basic (Beginner level)
    - **Japanese**: Basic (Beginner level)
    """)  # List your language proficiencies
    st.write("---")

    # Optional Contact Information (uncomment this section if you want to include contact info)
    # st.header("📧 Let's Connect")  # Subheading for contact info
    # st.write("""
    # Feel free to reach out to me via:
    # - **[Email](mailto:your-email@example.com)**  # Add a mailto link for your email
    # - **[LinkedIn](your-linkedin-url)**  # Add your LinkedIn profile link
    # - **[GitHub](https://github.com/arya-io)**  # Add your GitHub profile link
    # """)
