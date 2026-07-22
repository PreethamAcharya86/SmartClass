import streamlit as st
from src.components.header import header_home
def home_screen() :
    header_home()

    if st.button("Student", type='primary') :
        st.session_state['login_type'] = "student"
        st.rerun()
    if st.button("Teacher", type='primary') :
        st.session_state['login_type'] = "teacher"
        st.rerun()