import streamlit as st

def display_home():
    st.markdown(
        """
        <style>
        body {
            background-color: #f7f9fc;
            font-family: 'Arial', sans-serif;
        }
        .header {
            text-align: center;
            padding: 0px 0 50px 0; /* Increased bottom padding for more space below the header */
            color: #2c3e50;
        }
        
        .header h1 {
            font-size: 4.5em;
            font-weight: bold;
            margin-bottom: 20px; /* Increased space below the title */
            text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2); /* Slight text shadow */
        }
        
        .header h2 {
            font-size: 2.5em;
            font-weight: 300;
            color: #2980b9;
            margin-bottom: 50px; /* Increased space below the subtitle */
            text-transform: uppercase;
        }
        
        .introduction {
            text-align: center;
            font-size: 1.4em;
            line-height: 1.6;
            color: #555555;
            padding: 40px 60px; /* Increased padding for better spacing inside the box */
            background-color: #ffffff;
            border-radius: 15px;
            box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.1);
            margin: 40px auto; /* Added margin on top to create more space between sections */
            max-width: 800px;
            border: 1px solid #2980b9;
        }
        
        .quote {
            font-size: 1.8em;
            font-style: italic;
            text-align: center;
            margin: 60px 0; /* Increased vertical margin for more space above and below the quote */
            color: #2c3e50;
            background-color: #ecf0f1;
            padding: 30px; /* Increased padding for better spacing inside the quote box */
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
            max-width: 700px;
            margin: 40px auto; /* Adjusted for consistent vertical spacing */
            border: 2px solid #2980b9;
        }
        
        .footer {
            text-align: center;
            padding: 20px 0; /* Added padding to the footer for spacing */
            font-size: 1em;
            color: #888;
            position: relative;
            bottom: 0;
            width: 100%;
            margin-top: 80px; /* Increased space between footer and content above */
        }
        
        .footer img {
            width: 35px;
            margin: 0 15px;
            transition: opacity 0.3s;
            padding: 5px;
        }

        .footer a:hover img {
            opacity: 0.8;  # Change the opacity of icons when hovered for a subtle effect
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Header Section with title and subtitle
    st.markdown("<div class='header'><h1>Welcome to Arya's Portfolio</h1><h2>Aspiring Data Scientist | AI Enthusiast</h2></div>", unsafe_allow_html=True)

    # Personal Introduction Section
    st.markdown("<div class='introduction'>Hi! I'm Arya, a passionate Data Scientist with a B.Tech degree in Artificial Intelligence. My journey revolves around Machine Learning, Data Science, and AI. I am excited about exploring technology to make a meaningful impact. Dive into my portfolio to discover my projects, experience, and achievements.</div>", unsafe_allow_html=True)

    # Inspirational Quote Section
    st.markdown("<div class='quote'>\"Learning never exhausts the mind.\" - Leonardo da Vinci</div>", unsafe_allow_html=True)

    # Footer with social media links (LinkedIn and GitHub)
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
