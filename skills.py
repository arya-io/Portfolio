import streamlit as st
from PIL import Image

def display_skills():
    # Set the title for the Skills section with an icon
    st.title("💻 Skills & Expertise")

    # Create two columns for better organization and UI layout
    col1, col2 = st.columns([2, 2])

    # Left Column (col1) - Programming Languages and Competitive Achievements
    with col1:
        # Subheader for Programming Languages section
        st.subheader("🔧 Programming Languages")
        # Display the list of programming languages
        st.write("""
        - **C**
        - **C++**
        - **Python**
        - **SQL**
        """)

        # Subheader for Competitive Programming & Achievements section
        st.subheader("🏆 Competitive Programming & Achievements")
        # Display achievements such as coding ranks and typing speed
        st.write("""
        - **CodeChef**: 2-star coder.
        - **Typing Speed**: 55+ WPM.
        """)

    # Right Column (col2) - Web Scraping, Automation, and Cloud Platforms
    with col2:
        # Subheader for Web Scraping & Automation skills
        st.subheader("🔍 Web Scraping & Automation")
        # List of scraping and automation tools
        st.write("""
        - **Selenium**
        - **BeautifulSoup**
        """)

        # Subheader for Cloud Platforms
        st.subheader("☁️ Cloud Platforms")
        # Mention cloud-related achievements and experiences
        st.write("""
        - Completed **Google Cloud Ready Facilitator Program** in 2022.
        """)

    # Add a horizontal line for separation between sections
    st.markdown("---")

    # Expandable section for Data Analysis, Machine Learning, and AI tools
    with st.expander("📊 Data Analysis, Machine Learning & AI Tools"):
        # Detailed list of tools and libraries used for data-related tasks
        st.write("""
        I have experience working with various tools and libraries for data analysis, machine learning, and artificial intelligence:
        - **Pandas**, **Numpy** (Data manipulation and analysis)
        - **Scikit-learn** (Machine Learning algorithms)
        - **Matplotlib**, **Seaborn** (Data visualization)
        - **Computer Vision** (Image processing tasks)
        """)

    # Expandable section for Data Visualization & Dashboards
    with st.expander("📊 Data Visualization & Dashboards"):
        # Mention of dashboard tools and visualization libraries
        st.write("""
        I have used various tools for data visualization and dashboards:
        - **Matplotlib**, **Seaborn** (Data visualization libraries)
        - **Power BI**, **Excel** (Dashboard creation and analysis)
        """)

    # Subheader for Frameworks & Libraries section
    st.subheader("🛠️ Frameworks & Libraries")
    # Mention of frameworks with a focus on Streamlit
    st.write("""
    - **Streamlit**: Proficient in developing web applications and dashboards.
    """)

    # Subheader for Version Control and Collaboration section
    st.subheader("🔗 Version Control & Collaboration")
    # Mention of version control tools and collaboration goals
    st.write("""
    I am actively learning and using **Git** and **GitHub** to enhance my skills in version control and documentation. I aim to contribute to open-source projects soon.
    """)

    # Subheader for Soft Skills section
    st.subheader("💼 Soft Skills")
    # Mention of soft skills such as problem-solving and communication
    st.write("""
    - **Problem-Solving**
    - **Collaboration**
    - **Communication**
    - **Time Management**
    """)

    # Closing Section with a Call to Action for collaboration, displayed in the center of the page
    st.markdown(
        """
        <div style='text-align: center;'>
            <h4>Interested in collaborating? <a href='mailto:aryabharne7@gmail.com'>Let's get in touch!</a></h4>
        </div>
        """,
        unsafe_allow_html=True
    )
