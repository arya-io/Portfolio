import streamlit as st

def display_experience():
    # Header for Experience section with an icon
    st.header("💼 Experience")
    # Introduction text
    st.write("Explore my professional journey and the contributions I've made:")

    # Horizontal divider line
    st.markdown("---")

    # Define experience details as a list of dictionaries for each job role
    experiences = [
        {
            "company": "IPL Scoop",
            "position": "Data Scientist",
            "duration": "6 Months (Dec 2023 - June 2024)",
            "location": "Bengaluru (Remote)",
            # Key responsibilities in markdown format
            "responsibilities": """
            - Developed the **'Run Chase Prediction in IPL'** project for real-time insights.
            - Managed and grew the company's cricket Twitter (now X) account, engaging with a wide audience.
            - Improved existing features and enhanced prediction accuracy through innovative techniques.
            - Collaborated closely with the team to ensure project success and timely delivery.
            """,
            # List of technologies used during the project
            "technologies": ["Python", "Numpy", "Pandas", "Scikit-learn", "Matplotlib", "Streamlit", "pickle"],
            # Key achievements
            "achievements": """
            - **Grew Twitter followers** from 48 to over 1000, enabling monetization.
            - Successfully deployed the **Run Chase Prediction project** using Streamlit.
            - Integrated advanced visualizations for enhanced user engagement and clarity.
            """,
            # Challenges faced during the project
            "challenges": """
            - Sourced **historical IPL data** with inconsistencies in team names and incomplete records.
            - Preprocessed data thoroughly to ensure accurate model predictions.
            - Integrated interactive data visualizations to improve user insights and experience.
            """
        },
        # More experiences can be added in this format if needed
    ]

    # Loop through each experience and display details
    for exp in experiences:
        # Display position and company name as a subheader with an icon
        st.subheader(f"📍 {exp['position']} at {exp['company']}")
        # Display duration of the experience
        st.write(f"**Duration**: {exp['duration']}")
        # Display location of the role
        st.write(f"**Location**: {exp['location']}")

        # Section for key responsibilities
        st.markdown("### Key Responsibilities")
        st.markdown(exp['responsibilities'])

        # Display technologies used in the project
        st.markdown("**Technologies Used**: " + ', '.join(exp['technologies']))

        # Section for achievements
        st.markdown("### Achievements")
        st.markdown(exp['achievements'])

        # Section for challenges faced during the experience
        st.markdown("### Challenges Faced")
        st.markdown(exp['challenges'])

        # Horizontal divider line to separate each experience
        st.markdown("---")
