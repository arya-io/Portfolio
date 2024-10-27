import streamlit as st
from home import display_home
from about import display_about
from skills import display_skills
from projects import display_projects
from experience import display_experience
from education import display_education
from contact import display_contact

st.set_page_config(page_title="Arya's Portfolio", page_icon='💻')

st.sidebar.title('Navigation')
option = st.sidebar.radio('Go To', ('Home', 'About', 'Skills', 'Projects', 'Experience', 'Education', 'Contact'))

# Based on the option selected, call the respective function
if option == 'Home':
    display_home()
elif option == 'About':
    display_about()
elif option == 'Skills':
    display_skills()
elif option == 'Projects':
    display_projects()
elif option == 'Experience':
    display_experience()
elif option == 'Education':
    display_education()
elif option == 'Contact':
    display_contact()
