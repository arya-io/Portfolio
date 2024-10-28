import streamlit as st
from home import display_home
from about import display_about
from skills import display_skills
from projects import display_projects
from experience import display_experience
from education import display_education
from contact import display_contact

# Page Configurations
st.set_page_config(
    page_title="Arya's Portfolio",
    page_icon='💻',
    layout='wide',  # Expands content width
    initial_sidebar_state='expanded',
)

# Add custom styling for a more polished look
st.markdown("""
    <style>
        .main { 
            background-color: #f0f2f6; 
            font-family: 'Arial', sans-serif; 
        }
        .sidebar .sidebar-content { 
            background-color: #2f3136; 
            color: white; 
        }
        .sidebar .sidebar-content h2, 
        .sidebar-content h4 {
            color: #1ed760;
        }
        .profile-pic {
            border-radius: 50%;
            width: 100px;
            height: 100px;
            margin-bottom: 10px;
        }
        .greeting {
            font-size: 1.1rem;
            color: #1ed760;
            text-align: center;  /* Centered greeting */
        }
        .details {
            font-size: 0.85rem;
            color: #ffffff;
            text-align: center;  /* Centered details */
            margin-top: 5px;
        }
        .stRadio > label {
            color: white;
        }
        .stRadio > div > div:first-child {
            background-color: #1ed760;
            color: black;
        }
        .stRadio > div > div > label {
            color: white;
        }
        .stRadio > div > div:hover {
            background-color: #35a852;
        }
        .footer {
            text-align: center; 
            margin-top: 2rem;
            font-size: 0.8rem; 
            color: #555;
        }
        .social-links a {
            margin-right: 10px; 
            text-decoration: none; 
        }
        .social-links img {
            width: 25px; 
            height: 25px; 
        }
    </style>
""", unsafe_allow_html=True)

# Greeting based on time of day
import datetime
current_hour = datetime.datetime.now().hour
if current_hour < 12:
    greeting = "🌞 Good Morning!"
elif 12 <= current_hour < 18:
    greeting = "🌤 Good Afternoon!"
else:
    greeting = "🌙 Good Evening!"

# Moved greeting to the top of the sidebar
st.sidebar.markdown(f"<div class='greeting'>{greeting}</div>", unsafe_allow_html=True)
st.sidebar.markdown("""


""")

# Profile Section
st.sidebar.image("Arya.jpg", caption="", use_column_width=True, width=100)  # Update the path to your profile photo
st.sidebar.markdown("<h2 style='text-align: center; color: #1ed760;'>Arya</h2>", unsafe_allow_html=True)

# Additional Details
st.sidebar.markdown("""
    <div class='details'>
    AI Enthusiast
                    
    Nagpur, India
    </div>
""", unsafe_allow_html=True)

# Sidebar Navigation
option = st.sidebar.radio('Go To', 
    ('🏠 Home', '🧑‍💻 About', '📊 Skills', '📂 Projects', '💼 Experience', '🎓 Education', '📧 Contact'),
)

# Sidebar footer with social links
st.sidebar.markdown("""---""")
st.sidebar.markdown("""
    Connect with me:
                    
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/your-linkedin-url)
    [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github)](https://github.com/arya-io)
""")

# Based on the option selected, call the respective function
if option == '🏠 Home':
    display_home()
elif option == '🧑‍💻 About':
    display_about()
elif option == '📊 Skills':
    display_skills()
elif option == '📂 Projects':
    display_projects()
elif option == '💼 Experience':
    display_experience()
elif option == '🎓 Education':
    display_education()
elif option == '📧 Contact':
    display_contact()

# Footer at the bottom of the page
st.markdown("""
    <hr style='border: 1px solid #eaeaea;' />
    <div class='footer'>
        <small>© 2024 Arya's Portfolio. All rights reserved.</small>
    </div>
""", unsafe_allow_html=True)
