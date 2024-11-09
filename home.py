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
            padding: 0px 0 40px 0;  /* Increased bottom padding for more space below the header */
            color: #2c3e50;
        }
        .header h1 {
            font-size: 4.2em;
            font-weight: bold;
            margin-bottom: 10px;  /* Increased space below the title */
            text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
        }
        .header h2 {
            font-size: 2.2em;
            font-weight: 300;
            color: #2980b9;
            margin-bottom: 20px;  /* Increased space below the subtitle */
            text-transform: uppercase;
        }
        /* Updated Introduction section */
        .introduction {
            text-align: center;
            font-size: 1.3em;
            line-height: 1.8;  /* Increased line spacing for readability */
            color: #555555;
            padding: 30px;  /* Reduced padding for better centering */
            background-color: #ffffff;
            border-radius: 15px;
            box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.1);
            margin: 20px auto;  /* Reduced margin to align better */
            max-width: 700px;  /* Reduced max-width for better centering */
            border: 1px solid #2980b9; /* Border for emphasis */
        }
        /* Updated Quote section */
        .quote {
            font-size: 1.8em;
            font-style: italic;
            text-align: center;
            margin: 40px auto;  /* Reduced margin for better spacing */
            color: #2c3e50;
            background-color: #ecf0f1;
            padding: 20px;  /* Adjusted padding for better centering */
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
            max-width: 600px;  /* Reduced max-width for better centering */
            border: 2px solid #2980b9; /* Border for emphasis */
        }
        /* Updated Footer section */
        .footer {
            text-align: center;
            padding: 0px 0;  /* Added padding to better separate footer content */
            font-size: 1em;
            color: #888;
            width: 100%;
            margin-top: 50px;  /* Reduced margin to bring footer closer to content */
        }
        .footer img {
            width: 35px; /* Consistent icon size */
            margin: 0 10px; /* Reduced space between icons */
            transition: opacity 0.3s;
            padding: 5px;
        }
        .footer a:hover img {
            opacity: 0.8;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Header Section
    st.markdown("""
        <div class='header'>
            <h1>Welcome to Arya's Portfolio</h1>
            <h2>Aspiring Data Scientist | AI Enthusiast</h2>
        </div>
        """, unsafe_allow_html=True)

    # Personal Introduction
    st.markdown("""
        <div class='introduction'>
            Hi! I'm Arya, a passionate Data Scientist with a B.Tech degree in Artificial Intelligence. 
            My journey revolves around Machine Learning, Data Science, and AI. 
            I am excited about exploring technology to make a meaningful impact. 
            Dive into my portfolio to discover my projects, experience, and achievements.
        </div>
        """, unsafe_allow_html=True)

    # Inspirational Quote
    st.markdown("""
        <div class='quote'>
            "Learning never exhausts the mind." - Leonardo da Vinci
        </div>
        """, unsafe_allow_html=True)

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
