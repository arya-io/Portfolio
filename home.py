import streamlit as st
from PIL import Image

def display_home():
    # Set page title and background color
    st.markdown(
        """
        <style>
        body {
            background-color: #f7f9fc;
            font-family: 'Arial', sans-serif;
        }
        .header {
            text-align: center;
            padding: 0px 0 40px 0;
            color: #2c3e50;
        }
        .header h1 {
            font-size: 4.2em;
            font-weight: bold;
            color: white
            margin-bottom: 10px;
            text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
        }
        .header h2 {
            font-size: 2.2em;
            font-weight: 300;
            color: #2980b9;
            margin-bottom: 10px;
            text-transform: uppercase;
        }
        .introduction {
            text-align: center;
            font-size: 1.3em;
            line-height: 1.8;
            color: #555555;
            padding: 30px;
            background-color: #ffffff;
            border-radius: 15px;
            box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.1);
            margin: 20px auto;
            max-width: 700px;
            border: 1px solid #2980b9;
        }
        .quote {
            font-size: 1.8em;
            font-style: italic;
            text-align: center;
            margin: 40px auto;
            color: #2c3e50;
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            border: 2px solid #2980b9;
        }
        .footer {
            text-align: center;
            padding: 0px 0;
            font-size: 1em;
            color: #888;
            width: 100%;
            margin-top: 50px;
        }
        .footer img {
            width: 35px;
            margin: 0 10px;
            transition: opacity 0.3s;
            padding: 5px;
        }
        .footer a:hover img {
            opacity: 0.8;
        }
        </style>
        """, unsafe_allow_html=True
    )

    cols = st.columns([1, 7, 1])

    # Header Section
    st.cols[1].markdown("""
        <div class='header'>
            <h1>Welcome to Arya's Portfolio</h1>
            <h2>Aspiring Data Scientist | AI Enthusiast</h2>
        </div>
        """, unsafe_allow_html=True)

    image = Image.open("Arya.jpg")  # Load the image from the specified file path
    st.columns(3)[1].image(image, caption="Arya", use_column_width=None, width=360)    

    # Personal Introduction
    st.columns(3)[1].markdown("""
        <div class='introduction'>
            Hi! I'm Arya, a passionate Data Scientist with a B.Tech degree in Artificial Intelligence. 
            My journey revolves around Machine Learning, Data Science, and AI. 
            I am excited about exploring technology to make a meaningful impact. 
            Dive into my portfolio to discover my projects, experience, and achievements.
        </div>
        """, unsafe_allow_html=True)

    # Inspirational Quote
    st.columns(3)[1].markdown("""
        <div class='quote'>
            "Learning never exhausts the mind." - Leonardo da Vinci
        </div>
        """, unsafe_allow_html=True)

    # Footer with social media links
    st.columns(3)[1].markdown("""
        <footer class='footer'>
            <div>
                <a href='https://linkedin.com/in/aryaai' target='_blank'>
                    <img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' alt='LinkedIn' />
                </a>
                <a href='https://github.com/arya-io' target='_blank'>
                    <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' alt='GitHub' />
                </a>
            </div>
        </footer>
        """, unsafe_allow_html=True)
