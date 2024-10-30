import streamlit as st

def display_education():
    
    # Education Header with an icon
    st.markdown("<h1 style='text-align: center;'>🎓 Education</h1>", unsafe_allow_html=True)
    # Display the main header for the Education section with a graduation cap emoji, center-aligned

    # B.Tech Degree Section
    st.markdown("### <span style='color:#4CAF50;'>B.Tech in Artificial Intelligence</span>", unsafe_allow_html=True)
    # Subheader for B.Tech degree in AI with green color (#4CAF50) for emphasis
    st.markdown("**G. H. Raisoni College of Engineering, Nagpur**")
    # Display the name of the college in bold
    st.markdown("**Graduation Year**: 2024 | **CGPA**: 8.89")
    # Show graduation year and CGPA in bold for a clearer layout

    # List of Key Subjects Studied
    st.markdown("""
    <h4 style='margin-top: 10px;'>Key Subjects</h4>
    <ul>
        <li>Machine Learning and Algorithms</li>
        <li>Machine Learning with Tensorflow</li>
        <li>Foundation of Data Analytics</li>
        <li>Artificial Intelligence - Knowledge Representation and Reasoning</li>
        <li>Data Preprocessing</li>
        <li>Business Intelligence</li>
        <li>Cloud Computing</li>
        <li>Database Management Systems</li>
        <li>Natural Language Processing</li>
        <li>Soft Computing</li>
        <li>Big Data Computing</li>
        <li>Computer Vision and Deep Learning</li>
        <li>Design and Analysis of Algorithms</li>
        <li>Data Visualization</li>
    </ul>
    """, unsafe_allow_html=True)
    # Display a list of key subjects covered during the B.Tech program in Artificial Intelligence

    # Achievements Section
    st.markdown("""
    <h4 style='margin-top: 10px;'>Achievements</h4>
    <ul>
        <li><strong>GATE 2024 Qualified</strong> in Data Science and Artificial Intelligence (DA).</li>
        <li><strong>Published Research Papers</strong>:
            <ul>
                <li><em>Traffic Sign Viewer: An Enhanced Visibility of Traffic Signs for Better Awareness to Improve Transporter/Passenger Safety</em> – Published in IJCRT.</li>
                <li><em>A Comparative Study of Machine Learning Algorithms for Run Chase Prediction in IPL</em> – Published in IJSREM.</li>
            </ul>
        </li>
        <li><strong>Copyright</strong>: Received copyright from the Government of India for a poster titled <em>Composite Material Property Prediction Using Machine Learning Algorithm</em>.</li>
    </ul>
    """, unsafe_allow_html=True)
    # Display major academic achievements, including GATE qualification, published research papers, and a government copyright

    # Add a horizontal line to separate sections
    st.markdown("<hr>", unsafe_allow_html=True)

    # 12th Grade Education Section
    st.markdown("### <span style='color:#4CAF50;'>12th (Science - General)</span>", unsafe_allow_html=True)
    # Subheader for 12th-grade education with green color for emphasis
    st.markdown("**Shri Shivaji Science College, Nagpur**")
    # Display the name of the school in bold
    st.markdown("**Completion Year**: 2020 | **Percentage**: 84.15%")
    # Show completion year and percentage in bold

    # Horizontal line to separate sections
    st.markdown("<hr>", unsafe_allow_html=True)

    # 10th Grade Education Section
    st.markdown("### <span style='color:#4CAF50;'>10th CBSE</span>", unsafe_allow_html=True)
    # Subheader for 10th-grade education with green color for emphasis
    st.markdown("**St. Paul High School, Nagpur**")
    # Display the name of the school in bold
    st.markdown("**Completion Year**: 2018 | **Percentage**: 91.60%")
    # Show completion year and percentage in bold

    # Horizontal line to separate sections
    st.markdown("<hr>", unsafe_allow_html=True)

    # Certifications Section
    st.markdown("### <span style='color:#4CAF50;'>Certifications</span>", unsafe_allow_html=True)
    # Subheader for certifications with green color for emphasis
    st.markdown("""
    <ul>
        <li><strong>KLiC Certificate in C++ Programming</strong> – <em>Maharashtra Knowledge Corporation Ltd.</em> | January 2022</li>
        <li><strong>Google Cloud Facilitator Program</strong></li>
    </ul>
    """, unsafe_allow_html=True)
    # Display certifications earned, including a C++ programming certificate and Google Cloud Facilitator program participation

    # Horizontal line to separate sections
    st.markdown("<hr>", unsafe_allow_html=True)

    # Extracurricular Activities Section
    st.markdown("### <span style='color:#4CAF50;'>Extracurricular Activities</span>", unsafe_allow_html=True)
    # Subheader for extracurricular activities with green color for emphasis
    st.markdown("""
    <ul>
        <li>Participated in <strong>Smart India Hackathon</strong> and <strong>Maharashtra State Innovation Challenge</strong>.</li>
        <li>Competed in <strong>Coding Contests</strong> organized in college.</li>
        <li>Secured <strong>2nd Runner-up</strong> position in the <strong>Gandhi Jayanti Sketch Competition</strong>.</li>
        <li>Attended the <strong>AI Summit</strong> and <strong>Web Development Seminar</strong> organized at college.</li>
    </ul>
    """, unsafe_allow_html=True)
    # Display extracurricular achievements such as hackathon participation, coding contests, and events attended
