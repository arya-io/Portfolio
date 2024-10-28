import streamlit as st

def display_contact():
    # Header Section with Introduction
    st.header("📞 Contact Me")
    st.write("I would love to hear from you! Whether it's about collaborations, project inquiries, or exciting opportunities, here are the best ways to reach me:")

    # Divider Line
    st.markdown("<hr style='border:1px solid #f63366;'>", unsafe_allow_html=True)

    # Create Columns for better layout
    col1, col2, col3 = st.columns(3)

    # Email Section
    with col1:
        st.markdown("<h3 style='text-align: center;'>📧 Email</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Reach out via email:</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><a href='mailto:aryabharne7@gmail.com' style='text-decoration: none; color: #f63366; font-weight: bold;'>📨 aryabharne7@gmail.com</a></p>", unsafe_allow_html=True)

    # LinkedIn Section
    with col2:
        st.markdown("<h3 style='text-align: center;'>🔗 LinkedIn</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Connect with me:</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><a href='https://linkedin.com/in/aryaai' style='text-decoration: none; color: #0072b1; font-weight: bold;'>🔗 Visit my LinkedIn</a></p>", unsafe_allow_html=True)

    # GitHub Section (adjusted for visibility)
    with col3:
        st.markdown("<h3 style='text-align: center;'>💻 GitHub</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Explore my projects:</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><a href='https://github.com/arya-io' style='text-decoration: none; color: #f5f5f5; font-weight: bold;'>💻 Visit my GitHub</a></p>", unsafe_allow_html=True)  # Changed color to #f5f5f5 (light gray)

    # Another Divider Line
    st.markdown("<hr style='border:1px solid #f63366;'>", unsafe_allow_html=True)

    # Footer Message with Center Alignment
    st.markdown("<p style='text-align: center; font-size: 18px;'>Looking forward to hearing from you soon!</p>", unsafe_allow_html=True)