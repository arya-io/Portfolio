import streamlit as st
from PIL import Image

def display_skills():
    # Set page title
    st.title("💻 Skills & Expertise")

    # Split sections into columns for better UI
    col1, col2 = st.columns([2, 2])

    with col1:
        # Programming Languages
        st.subheader("🔧 Programming Languages")
        st.write("""
        - **C**
        - **C++**
        - **Python**
        - **SQL**
        """)

        # Competitive Programming / Other Achievements
        st.subheader("🏆 Competitive Programming & Achievements")
        st.write("""
        - **CodeChef**: 2-star coder.
        - **Typing Speed**: 60 WPM.
        """)

    with col2:
        # Web Scraping & Automation
        st.subheader("🔍 Web Scraping & Automation")
        st.write("""
        - **Selenium**
        - **BeautifulSoup**
        """)

        # Cloud Platforms
        st.subheader("☁️ Cloud Platforms")
        st.write("""
        - Completed **Google Cloud Facilitator Program** in 2022.
        """)

    # Add a separator
    st.markdown("---")

    # Expandable section for more technical details
    with st.expander("📊 Data Analysis, Machine Learning & AI Tools"):
        st.write("""
        I have experience working with various tools and libraries for data analysis, machine learning, and artificial intelligence:
        - **Pandas**, **Numpy** (Data manipulation and analysis)
        - **Scikit-learn** (Machine Learning algorithms)
        - **Matplotlib**, **Seaborn** (Data visualization)
        - **Computer Vision** (Image processing tasks)
        """)

    with st.expander("📊 Data Visualization & Dashboards"):
        st.write("""
        I have used various tools for data visualization and dashboards:
        - **Matplotlib**, **Seaborn** (Data visualization libraries)
        - **Power BI**, **Excel** (Dashboard creation and analysis)
        """)

    # Frameworks and Libraries
    st.subheader("🛠️ Frameworks & Libraries")
    st.write("""
    - **Streamlit**: Proficient in developing web applications and dashboards.
    """)

    # Version Control
    st.subheader("🔗 Version Control & Collaboration")
    st.write("""
    I am actively learning and using **Git** and **GitHub** to enhance my skills in version control and documentation. I aim to contribute to open-source projects soon.
    """)

    # Soft Skills
    st.subheader("💼 Soft Skills")
    st.write("""
    - **Problem-Solving**
    - **Collaboration**
    - **Communication**
    - **Time Management**
    """)

    # Closing Section: Call to Action
    st.markdown(
        """
        <div style='text-align: center;'>
            <h4>Interested in collaborating? <a href='mailto:aryabharne7@gmail.com'>Let's get in touch!</a></h4>
        </div>
        """,
        unsafe_allow_html=True
    )