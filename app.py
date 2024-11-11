import streamlit as st
from home import display_home
from about import display_about
from skills import display_skills
from projects import display_projects
from experience import display_experience
from education import display_education
from contact import display_contact

st.set_page_config(
    page_title="Arya's Portfolio",
    page_icon='💻',
    layout='wide',
    initial_sidebar_state='expanded',
)

st.markdown("""
    <style>
        .main { 
            background-color: #f0f2f6;  # Sets the background color for the main content
            font-family: 'Arial', sans-serif;  # Uses Arial font
        }
        .sidebar .sidebar-content { 
            background-color: #2f3136;  # Dark background for the sidebar
            color: white;  # White text color for the sidebar
        }
        .footer {
            text-align: center;  # Centers the footer text
            margin-top: 2rem;  # Adds space above the footer
            font-size: 0.8rem;  # Smaller font size for footer
            color: #555;  # Gray text color for the footer
        }
        .details {
            font-size: 0.85rem;
            color: #ffffff;
            text-align: center;  /* Centered details */
            margin-top: 2px;
        }
        .greeting {
            font-size: 1.1rem;
            color: #1ed760;
            text-align: center;  /* Centered greeting */
            margin-bottom: 12px
        }
    </style>
""", unsafe_allow_html=True)

# Greeting based on time of day
import datetime
current_hour = datetime.datetime.now().hour + 6 # Get the current hour
if current_hour < 12:
    greeting = "🌞 Good Morning!"
elif 12 <= current_hour < 18:
    greeting = "🌤 Good Afternoon!"
else:
    greeting = "🌙 Good Evening!"

st.sidebar.markdown(f"<div class='greeting'>{greeting}</div>", unsafe_allow_html=True)  # Display greeting in sidebar

# st.sidebar.markdown("""---""")

st.sidebar.image("Arya.jpg", caption="", use_column_width=True, width=100)  # Displays profile image in sidebar
st.sidebar.markdown("<h2 style='text-align: center; color: #1ed760;'>Arya</h2>", unsafe_allow_html=True)  # Name below the image

st.sidebar.markdown("""
    <div class='details'>
    AI Enthusiast
    </div>
""", unsafe_allow_html=True)
st.sidebar.markdown("""
    <div class='details'>
    Nagpur, India
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""---""")

option = st.sidebar.radio('Go To', 
    ('🏠 Home', '🧑‍💻 About', '📊 Skills', '📂 Projects', '💼 Experience', '🎓 Education', '📧 Contact'),
)  # Radio buttons for navigation between sections of the portfolio

# Sidebar footer with social links
st.sidebar.markdown("""---""")
st.sidebar.markdown("""
    Connect with me:
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/your-linkedin-url)
    [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github)](https://github.com/arya-io)
""")  # Displays clickable LinkedIn and GitHub badges

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
