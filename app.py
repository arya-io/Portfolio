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
        .main { background-color: #f0f2f6; }
        .sidebar .sidebar-content { background-color: #2f3136; color: white; }
        .sidebar .sidebar-content h2, .sidebar-content h4 {
            color: #1ed760;
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
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation with Icons
st.sidebar.title('📂 Navigation')
option = st.sidebar.radio('Go To', 
    ('🏠 Home', '🧑‍💻 About', '📊 Skills', '📂 Projects', '💼 Experience', '🎓 Education', '📧 Contact'),
)

# Display dynamic greeting on the sidebar based on time of day
import datetime
current_hour = datetime.datetime.now().hour
if current_hour < 12:
    greeting = "🌞 Good Morning!"
elif 12 <= current_hour < 18:
    greeting = "🌤 Good Afternoon!"
else:
    greeting = "🌙 Good Evening!"

st.sidebar.markdown(f"### {greeting}")

# Sidebar footer with social links
st.sidebar.markdown("""
    ---
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
    <div style='text-align: center;'>
        <small>© 2024 Arya's Portfolio. All rights reserved.</small>
    </div>
""", unsafe_allow_html=True)
