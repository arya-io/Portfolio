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
    page_title="Arya's Portfolio",  # Title of the browser tab
    page_icon='💻',  # Icon shown in the browser tab
    layout='wide',  # Expands content width to full screen
    initial_sidebar_state='expanded',  # Sidebar is expanded by default
)

# Add custom styling for a more polished look using HTML and CSS
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
        .sidebar .sidebar-content h2, 
        .sidebar-content h4 {
            color: #1ed760;  # Light green for headings in the sidebar
        }
        .profile-pic {
            border-radius: 50%;  # Makes profile picture circular
            width: 100px;  # Sets the width of the profile picture
            height: 100px;  # Sets the height of the profile picture
            margin-bottom: 10px;  # Adds space below the profile picture
        }
        .greeting {
            font-size: 1.1rem;  # Sets the font size for greeting text
            color: #1ed760;  # Green text color for greeting
            text-align: center;  # Centers the greeting text
        }
        .details {
            font-size: 0.85rem;  # Smaller text for additional details
            color: #ffffff;  # White text color for details
            text-align: center;  # Centers the additional details
            margin-top: 5px;  # Adds space above the details
        }
        .stRadio > label {
            color: white;  # White text for radio buttons
        }
        .stRadio > div > div:first-child {
            background-color: #1ed760;  # Green background for selected radio button
            color: black;  # Black text for selected radio button
        }
        .stRadio > div > div > label {
            color: white;  # White text for other radio buttons
        }
        .stRadio > div > div:hover {
            background-color: #35a852;  # Darker green background when hovered
        }
        .footer {
            text-align: center;  # Centers the footer text
            margin-top: 2rem;  # Adds space above the footer
            font-size: 0.8rem;  # Smaller font size for footer
            color: #555;  # Gray text color for the footer
        }
        .social-links a {
            margin-right: 10px;  # Adds space between social link icons
            text-decoration: none;  # Removes underline from social links
        }
        .social-links img {
            width: 25px;  # Sets the width of social media icons
            height: 25px;  # Sets the height of social media icons
        }
    </style>
""", unsafe_allow_html=True)  # Allows the use of HTML/CSS for custom styling

# Greeting based on time of day
import datetime
current_hour = datetime.datetime.now().hour  # Get the current hour
if current_hour < 12:
    greeting = "🌞 Good Morning!"  # Morning greeting
elif 12 <= current_hour < 18:
    greeting = "🌤 Good Afternoon!"  # Afternoon greeting
else:
    greeting = "🌙 Good Evening!"  # Evening greeting

# Moved greeting to the top of the sidebar
st.sidebar.markdown(f"<div class='greeting'>{greeting}</div>", unsafe_allow_html=True)  # Display greeting in sidebar

# Profile Section
st.sidebar.image("Arya1.jpg", caption="", use_column_width=True, width=100)  # Displays profile image in sidebar
st.sidebar.markdown("<h2 style='text-align: center; color: #1ed760;'>Arya</h2>", unsafe_allow_html=True)  # Name below the image

# Additional Details
st.sidebar.markdown("""
    <div class='details'>
    AI Enthusiast  # Description below the name
    Nagpur, India  # Location
    </div>
""", unsafe_allow_html=True)  # Display additional details like job title and location

# Sidebar Navigation
option = st.sidebar.radio('Go To', 
    ('🏠 Home', '🧑‍💻 About', '📊 Skills', '📂 Projects', '💼 Experience', '🎓 Education', '📧 Contact'),
)  # Radio buttons for navigation between sections of the portfolio

# Sidebar footer with social links
st.sidebar.markdown("""---""")  # Horizontal divider
st.sidebar.markdown("""
    Connect with me:
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/your-linkedin-url)
    [![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github)](https://github.com/arya-io)
""")  # Displays clickable LinkedIn and GitHub badges

# Based on the option selected, call the respective function
if option == '🏠 Home':
    display_home()  # Display home page content
elif option == '🧑‍💻 About':
    display_about()  # Display about page content
elif option == '📊 Skills':
    display_skills()  # Display skills page content
elif option == '📂 Projects':
    display_projects()  # Display projects page content
elif option == '💼 Experience':
    display_experience()  # Display experience page content
elif option == '🎓 Education':
    display_education()  # Display education page content
elif option == '📧 Contact':
    display_contact()  # Display contact page content

# Footer at the bottom of the page
st.markdown("""
    <hr style='border: 1px solid #eaeaea;' />  # Horizontal line for separation
    <div class='footer'>
        <small>© 2024 Arya's Portfolio. All rights reserved.</small>  # Footer text
    </div>
""", unsafe_allow_html=True)  # Display footer at the bottom of the page
