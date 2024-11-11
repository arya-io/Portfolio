import streamlit as st
from PIL import Image

def display_skills():

    st.title("💻 Skills & Expertise")

    # Create two columns for better organization and UI layout
    col1, col2 = st.columns([2, 2])

    # Left Column (col1) - Programming Languages Achievements
    with col1:
        st.subheader("🔧 Programming Languages")
        st.write("""
        - **C**
        - **C++**
        - **Python**
        - **SQL**
        """)

        # Subheader for Competitive Programming & Achievements section
        st.subheader("🏆 Achievements")
        st.write("""
        - **CodeChef**: 2-star coder.
        - **Typing Speed**: 55+ WPM.
        """)

    # Right Column (col2) - Web Scraping, Automation, and Cloud Platforms
    with col2:
        st.subheader("🔍 Web Scraping & Automation")
        st.write("""
        - **Selenium**
        - **BeautifulSoup**
        """)

        st.subheader("☁️ Cloud Platforms")
        st.write("""
        - Completed **Google Cloud Ready Facilitator Program** in 2022.
        """)

    st.write("---")
    
    # Section for Data Analysis, Machine Learning, and AI tools
    st.subheader("📊 Data Analysis, Machine Learning & AI Tools")
    st.write("""
    I have experience working with various tools and libraries for data analysis, machine learning, and artificial intelligence:
    - **Pandas**, **Numpy** (Data manipulation and analysis)
    - **Scikit-learn** (Machine Learning algorithms)
    - **Matplotlib**, **Seaborn** (Data visualization)
    - **Computer Vision** (Image processing tasks)
    """)
    
    st.write("---")
    
    # Subheader for Frameworks & Libraries section
    st.subheader("🛠️ Frameworks & Libraries")
    st.write("""
    - **Streamlit**: Proficient in developing web applications and dashboards.
    """)
    
    st.write("---")
    
    # Subheader for Version Control and Collaboration section
    st.subheader("🔗 Version Control & Collaboration")
    st.write("""
    I am actively learning and using **Git** and **GitHub** to enhance my skills in version control and documentation. I aim to contribute to open-source projects soon.
    """)
    
    st.write("---")
    
    # Subheader for Soft Skills section
    st.subheader("💼 Soft Skills")
    st.write("""
    - **Problem-Solving**
    - **Collaboration**
    - **Communication**
    - **Time Management**
    """)

    st.write("---")
    
    # Closing Section with a Call to Action for collaboration, displayed in the center of the page
    st.markdown(
        """
        <div style='text-align: center;'>
            <h4>Interested in collaborating? <a href='mailto:aryabharne7@gmail.com'>Let's get in touch!</a></h4>
        </div>
        """,
        unsafe_allow_html=True
    )
