import streamlit as st

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
            padding: 0px 0 30px 0;  /* Reduced top padding */
            color: #2c3e50;
        }
        .header h1 {
            font-size: 4.5em;
            font-weight: bold;
            margin-bottom: 10px;
            text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
        }
        .header h2 {
            font-size: 2.5em;
            font-weight: 300;
            color: #2980b9;
            margin-bottom: 40px;
            text-transform: uppercase;
        }
        .introduction {
            text-align: center;
            font-size: 1.4em;
            line-height: 1.6;
            color: #555555;
            padding: 30px 50px;
            background-color: #ffffff;
            border-radius: 15px;
            box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.1);
            margin: 0 auto;
            max-width: 800px;
            border: 1px solid #2980b9; /* Added border */
        }
        .quote {
            font-size: 1.8em;
            font-style: italic;
            text-align: center;
            margin: 50px 0;
            color: #2c3e50;
            background-color: #ecf0f1;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
            max-width: 700px;
            margin: 20px auto;
            border: 2px solid #2980b9; /* Added border */
        }
        .button {
            display: inline-block;
            background-color: #2980b9;
            color: #ffffff;
            padding: 15px 35px;
            font-size: 1.2em;
            border-radius: 5px;
            text-decoration: none;
            transition: background-color 0.3s, transform 0.3s; /* Added transform */
            margin: 20px 10px;
        }
        .button:hover {
            background-color: #1a5276;
            transform: translateY(-3px); /* Button lift effect */
        }
        .footer {
            text-align: center;
            padding: 0px;
            font-size: 1em;
            color: #888;
            position: relative;
            bottom: 0;
            width: 100%;
            margin-top: 60px;
        }
        .footer img {
            width: 35px; /* Increased icon size */
            margin: 0 15px;
            transition: opacity 0.3s;
            padding: 5px; /* Added padding */
        }
        .footer a:hover img {
            opacity: 0.8;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Header Section
    st.markdown("<div class='header'><h1>Welcome to Arya's Portfolio</h1><h2>Aspiring Data Scientist | AI Enthusiast</h2></div>", unsafe_allow_html=True)

    # Personal Introduction
    st.markdown("<div class='introduction'>Hi! I'm Arya, a passionate Data Scientist with a B.Tech degree in Artificial Intelligence. My journey revolves around Machine Learning, Data Science, and AI. I am excited about exploring technology to make a meaningful impact. Dive into my portfolio to discover my projects, experience, and achievements.</div>", unsafe_allow_html=True)

    # Inspirational Quote
    st.markdown("<div class='quote'>\"Learning never exhausts the mind.\" - Leonardo da Vinci</div>", unsafe_allow_html=True)

    # Footer with social media links
    st.markdown("""
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
