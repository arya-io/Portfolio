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
            padding: 0px 0 30px 0;  # Adjust the space around the header
            color: #2c3e50;
        }
        .header h1 {
            font-size: 4.5em;
            font-weight: bold;
            margin-bottom: 10px;  # Add space below the title
            text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);  # Add a slight shadow to the text for a 3D effect
        }
        .header h2 {
            font-size: 2.5em;
            font-weight: 300;
            color: #2980b9;
            margin-bottom: 40px;  # Add space below the subtitle
            text-transform: uppercase;  # Make all the letters in the subtitle uppercase
        }
        .introduction {
            text-align: center;
            font-size: 1.4em;
            line-height: 1.6;  # Increase line spacing for readability
            color: #555555;  # Set a neutral color for the text
            padding: 30px 50px;  # Add padding inside the introduction box
            background-color: #ffffff;  # Set a white background for the introduction box
            border-radius: 15px;  # Round the corners of the introduction box
            box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.1);  # Add a subtle shadow around the box
            margin: 0 auto;  # Center the box within the page
            max-width: 800px;  # Set a maximum width for the box
            border: 1px solid #2980b9;  # Add a border to the box for emphasis
        }
        .quote {
            font-size: 1.8em;
            font-style: italic;  # Italicize the text to differentiate it
            text-align: center;  # Center the quote text
            margin: 50px 0;  # Add space above and below the quote
            color: #2c3e50;  # Use a darker color for the quote text
            background-color: #ecf0f1;  # Set a light background color for the quote box
            padding: 25px;  # Add padding inside the quote box
            border-radius: 10px;  # Round the corners of the quote box
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);  # Add a slight shadow around the box
            max-width: 700px;  # Set a maximum width for the quote box
            margin: 20px auto;  # Center the quote box within the page
            border: 2px solid #2980b9;  # Add a border to the quote box for emphasis
        }
        .footer {
            text-align: center;
            padding: 0px;  # Remove padding around the footer
            font-size: 1em;  # Set a standard font size for the footer text
            color: #888;  # Set a light gray color for the footer text
            position: relative;  # Position the footer at the bottom
            bottom: 0;  # Align the footer with the bottom of the page
            width: 100%;  # Make the footer span the entire page width
            margin-top: 60px;  # Add space between the footer and content above
        }
        .footer img {
            width: 35px;  # Set the size of the social media icons
            margin: 0 15px;  # Add space between icons
            transition: opacity 0.3s;  # Add a smooth transition effect when hovering over icons
            padding: 5px;  # Add padding around the icons
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
