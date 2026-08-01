import streamlit as st
from src.screens.choice_screen import choice_screen 


def header_home() :
    st.header("Visual Attend", text_alignment="center")

def navbar() :
    c1, c2 = st.columns(2)
    with c1 :
        st.write("VISUAL ATTEND")
    with c2 :
        if  'teacher_data' in st.session_state and st.session_state.user_role == 'teacher':
            if st.button("Logout", key='logout') :
                del st.session_state.teacher_data
                st.session_state.user_role = None
                st.session_state.is_logged_in = False
                st.session_state['login_type'] = None

                st.rerun()

        elif 'student_data' in st.session_state and st.session_state.user_role == 'student':
            if st.button("Logout", key='logout') :
                del st.session_state.student_data
                st.session_state.user_role = None
                st.session_state.is_logged_in = False
                st.session_state['login_type'] = None
                st.rerun()

        else :
            if st.button("Get started") :
                st.session_state['login_type'] = 'choose'
                st.rerun()
        

def back() :
    if st.button('<--') :
        st.session_state['login_type'] = None
        st.rerun()
