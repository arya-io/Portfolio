import streamlit as st

def display_experience():
    st.header("💼 Experience")
    st.write("Explore my professional journey and the contributions I've made:")

    st.markdown("---")

    # Define experience details
    experiences = [
        {
            "company": "IPL Scoop",
            "position": "Data Scientist",
            "duration": "6 Months (Dec 2023 - June 2024)",
            "location": "Bengaluru (Remote)",
            "responsibilities": """
            - Developed the **'Run Chase Prediction in IPL'** project for real-time insights.
            - Managed and grew the company's cricket Twitter (now X) account, engaging with a wide audience.
            - Improved existing features and enhanced prediction accuracy through innovative techniques.
            - Collaborated closely with the team to ensure project success and timely delivery.
            """,
            "technologies": ["Python", "Numpy", "Pandas", "Scikit-learn", "Matplotlib", "Streamlit", "pickle"],
            "achievements": """
            - **Grew Twitter followers** from 48 to over 1000, enabling monetization.
            - Successfully deployed the **Run Chase Prediction project** using Streamlit.
            - Integrated advanced visualizations for enhanced user engagement and clarity.
            """,
            "challenges": """
            - Sourced **historical IPL data** with inconsistencies in team names and incomplete records.
            - Preprocessed data thoroughly to ensure accurate model predictions.
            - Integrated interactive data visualizations to improve user insights and experience.
            """
        },
        # Add more experiences here if needed
    ]

    # Display experience details directly without expanders
    for exp in experiences:
        st.subheader(f"📍 {exp['position']} at {exp['company']}")
        st.write(f"**Duration**: {exp['duration']}")
        st.write(f"**Location**: {exp['location']}")

        # Responsibilities
        st.markdown("### Key Responsibilities")
        st.markdown(exp['responsibilities'])

        # Technologies Used
        st.markdown("**Technologies Used**: " + ', '.join(exp['technologies']))

        # Achievements
        st.markdown("### Achievements")
        st.markdown(exp['achievements'])

        # Challenges Faced
        st.markdown("### Challenges Faced")
        st.markdown(exp['challenges'])

        st.markdown("---")