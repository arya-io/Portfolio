import streamlit as st
from PIL import Image

def display_projects():
    # Header for the projects section with an icon
    st.header("🚀 My Projects")
    # Introduction text for the projects section
    st.write("Here are some of my recent projects, categorized by domain. You can filter the projects by category or expand them for more details:")

    # Dictionary of project categories and corresponding icons
    icons = {
        "AI": "🧠",
        "Computer Vision": "👁️",
        "Data Science": "📊",
        "Machine Learning": "🤖",
        "Web Scraping": "🌐",
        "Automation": "🤖",
        "Exploratory Data Analysis": "🔍",
    }

    # Horizontal divider line
    st.markdown("---")

    # List of projects, each project is a dictionary with details such as name, category, description, tools used, and GitHub link
    projects = [
        {
            "name": "Hand Gesture Volume Control System",
            "category": ["AI", "Computer Vision"],
            "description": """In this project, I built a system to control the system's volume using hand gestures. 
            The system uses OpenCV to capture hand gestures, MediaPipe for hand-tracking, and Python to map gestures to volume control actions.""",
            "tools": ["Python", "OpenCV", "MediaPipe"],
            "link": "https://github.com/arya-io/AI-Volume-Controller.git",
        },
        {
            "name": "Run Chase Prediction in IPL",
            "category": ["AI", "Data Science", "Machine Learning"],
            "description": """This project predicts the chances of a team successfully chasing a target in IPL cricket matches. 
            Using historical IPL data and applying machine learning algorithms, I predicted match outcomes.""",
            "tools": ["Python", "Pandas", "Scikit-learn", "Streamlit"],
            "link": "https://github.com/arya-io/A-Machine-Learning-Approach-for-Run-Chase-Prediction-in-IPL.git",
        },
        {
            "name": "Flipkart Data Scraping",
            "category": ["Web Scraping"],
            "description": """A Python script to scrape product data such as names, prices, descriptions, and ratings from Flipkart.
            The project was useful for analyzing product trends and pricing.""",
            "tools": ["Python", "BeautifulSoup", "Selenium", "Pandas"],
            "link": "https://github.com/arya-io/Flipkart-Data-Scraping.git",
        },
        {
            "name": "Ajio Infinite Scroll Scraping",
            "category": ["Web Scraping", "Automation"],
            "description": """This project involved scraping data from Ajio, a fashion e-commerce platform with infinite scrolling. 
            I used Selenium to handle dynamic content loading and successfully scraped product data.""",
            "tools": ["Python", "Selenium"],
            "link": "https://github.com/arya-io/Ajio-Infinite-Scrolling-Bot.git",
        },
        {
            "name": "Telco Customer Churn EDA",
            "category": ["Data Science", "Exploratory Data Analysis"],
            "description": """Exploratory Data Analysis (EDA) on a Telco customer churn dataset to understand customer behavior and identify reasons for churn. 
            The analysis included visualizations and statistical summaries to help in decision-making.""",
            "tools": ["Python", "Pandas", "Matplotlib", "Seaborn"],
            "link": "https://github.com/arya-io/telco-customer-churn-eda.git",
        },
        {
            "name": "House of Dragons Web Automation",
            "category": ["Web Scraping", "Automation"],
            "description": """This project demonstrates web automation using Selenium to interact with Google Search. It automates the process 
            of searching for 'House of Dragons' on Google, capturing a screenshot of the results.""",
            "tools": ["Python", "Selenium", "Jupyter Notebook"],
            "link": "https://github.com/arya-io/house-of-dragons-web-automation.git",
        },
        {
            "name": "AI Background Changer",
            "category": ["AI", "Computer Vision"],
            "description": """This project allows users to upload a photo and change its background using AI. The application, built with 
            Streamlit and Cloudinary AI API, lets users enter a prompt to modify the background of an image. The transformed image can be downloaded.""",
            "tools": ["Python", "Streamlit", "Cloudinary AI API"],
            "link": "https://github.com/arya-io/AI-Background-Changer.git",
        },
    ]

    # Dropdown for filtering projects by category
    category = st.selectbox("Filter by category:", ["All"] + sorted(set([cat for project in projects for cat in project['category']])))

    # Loop through the list of projects and display those that match the selected category or show all if "All" is selected
    for project in projects:
        if category == "All" or category in project['category']:
            # Use an expander to display project details that the user can click to expand
            with st.expander(f"{icons.get(project['category'][0], '🚀')} **{project['name']}** ({', '.join(project['category'])})", expanded=False):
                # Display the project details in a card-like structure with markdown for better formatting
                st.markdown(f"""
                <div style='border: 1px solid #ddd; padding: 10px; border-radius: 5px;'>
                    <h4 style='color: #2d7d9a;'>{project['name']}</h4>
                    <p>{project['description']}</p>
                    <p><strong>Tools used:</strong> {' | '.join(project['tools'])}</p>
                    <a href="{project['link']}" target="_blank" style="color: #3E96FF; text-decoration: none;">
                        🔗 View Project on GitHub
                    </a>
                </div>
                """, unsafe_allow_html=True)

    # Horizontal divider line after the project list
    st.markdown("---")
