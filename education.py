import streamlit as st

def display_education():
    
    # Education Header with an icon
    st.markdown("<h1 style='text-align: center;'>🎓 Education</h1>", unsafe_allow_html=True)
    
    # B.Tech Degree Section
    st.markdown("### <span style='color:#4CAF50;'>B.Tech in Artificial Intelligence</span>", unsafe_allow_html=True)
    st.markdown("**G. H. Raisoni College of Engineering, Nagpur**")
    st.markdown("**Graduation Year**: 2024 | **CGPA**: 8.89")
    
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

    # Add a horizontal line
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # 12th Grade Section
    st.markdown("### <span style='color:#4CAF50;'>12th (Science - General)</span>", unsafe_allow_html=True)
    st.markdown("**Shri Shivaji Science College, Nagpur**")
    st.markdown("**Completion Year**: 2020 | **Percentage**: 84.15%")
    
    # Horizontal line
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # 10th Grade Section
    st.markdown("### <span style='color:#4CAF50;'>10th CBSE</span>", unsafe_allow_html=True)
    st.markdown("**St. Paul High School, Nagpur**")
    st.markdown("**Completion Year**: 2018 | **Percentage**: 91.60%")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Certifications Section
    st.markdown("### <span style='color:#4CAF50;'>Certifications</span>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><strong>KLiC Certificate in C++ Programming</strong> – <em>Maharashtra Knowledge Corporation Ltd.</em> | January 2022</li>
        <li><strong>Google Cloud Facilitator Program</strong></li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Extracurricular Activities Section
    st.markdown("### <span style='color:#4CAF50;'>Extracurricular Activities</span>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li>Participated in <strong>Smart India Hackathon</strong> and <strong>Maharashtra State Innovation Challenge</strong>.</li>
        <li>Competed in <strong>Coding Contests</strong> organized in college.</li>
        <li>Secured <strong>2nd Runner-up</strong> position in the <strong>Gandhi Jayanti Sketch Competition</strong>.</li>
        <li>Attended the <strong>AI Summit</strong> and <strong>Web Development Seminar</strong> organized at college.</li>
    </ul>
    """, unsafe_allow_html=True)