import streamlit as st

def display_contact():
    # Header Section with Introduction
    st.header("📞 Contact Me")
    # Display the header for the contact page with a phone emoji
    st.write("I would love to hear from you! Whether it's about collaborations, project inquiries, or exciting opportunities, here are the best ways to reach me:")
    # Provide a brief introduction, encouraging people to get in touch for various reasons

    # Divider Line
    st.markdown("<hr style='border:1px solid #f63366;'>", unsafe_allow_html=True)
    # Add a horizontal line (divider) with a custom color (#f63366) to separate sections

    # Create Columns for better layout
    col1, col2, col3 = st.columns(3)
    # Create three equal-width columns to neatly display different contact options

    # Email Section
    with col1:
        st.markdown("<h3 style='text-align: center;'>📧 Email</h3>", unsafe_allow_html=True)
        # Display a subheader for the Email section, center-aligned with an email emoji
        st.markdown("<p style='text-align: center;'>Reach out via email:</p>", unsafe_allow_html=True)
        # Center-aligned paragraph prompting the user to email
        st.markdown("<p style='text-align: center;'><a href='mailto:aryabharne7@gmail.com' style='text-decoration: none; color: #f63366; font-weight: bold;'>📨 aryabharne7@gmail.com</a></p>", unsafe_allow_html=True)
        # Create a mailto link that opens the user's default email client when clicked. The link has custom styling with bold, red text.

    # LinkedIn Section
    with col2:
        st.markdown("<h3 style='text-align: center;'>🔗 LinkedIn</h3>", unsafe_allow_html=True)
        # Display a subheader for the LinkedIn section, center-aligned with a LinkedIn icon
        st.markdown("<p style='text-align: center;'>Connect with me:</p>", unsafe_allow_html=True)
        # Center-aligned paragraph prompting the user to connect on LinkedIn
        st.markdown("<p style='text-align: center;'><a href='https://linkedin.com/in/aryaai' style='text-decoration: none; color: #0072b1; font-weight: bold;'>🔗 Visit my LinkedIn</a></p>", unsafe_allow_html=True)
        # Create a clickable link to the LinkedIn profile with custom styling using LinkedIn's brand color (#0072b1) for the link

    # GitHub Section
    with col3:
        st.markdown("<h3 style='text-align: center;'>💻 GitHub</h3>", unsafe_allow_html=True)
        # Display a subheader for the GitHub section, center-aligned with a laptop emoji
        st.markdown("<p style='text-align: center;'>Explore my projects:</p>", unsafe_allow_html=True)
        # Center-aligned paragraph prompting the user to explore GitHub projects
        st.markdown("<p style='text-align: center;'><a href='https://github.com/arya-io' style='text-decoration: none; color: #f5f5f5; font-weight: bold;'>💻 Visit my GitHub</a></p>", unsafe_allow_html=True)
        # Create a clickable link to the GitHub profile with custom styling using a light gray color (#f5f5f5) for better visibility

    # Another Divider Line
    st.markdown("<hr style='border:1px solid #f63366;'>", unsafe_allow_html=True)
    # Add another horizontal line with the same custom color to visually separate sections

    # Footer Message with Center Alignment
    st.markdown("<p style='text-align: center; font-size: 18px;'>Looking forward to hearing from you soon!</p>", unsafe_allow_html=True)
    # Display a footer message, center-aligned, with slightly larger font size (18px) to encourage users to reach out
