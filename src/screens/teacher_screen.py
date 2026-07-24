import streamlit as st
from src.components.header import back
from src.components.header import navbar
def teacher_screen() :
    back()

    if 'teacher' not in st.session_state or st.session_state.teacher == "login" :
        teacher_screen_login()
    elif st.session_state.teacher == "register" :
        teacher_screen_register()
    

def teacher_screen_login() :
    st.header('Login using password', text_alignment="center")

    teacher_username = st.text_input("User name", placeholder='Enter your username')
    teacher_password = st.text_input("Password",type="password", placeholder='Enter your password')

    st.divider()

    btn1, btn2 = st.columns(2)
    with btn1 :
        st.button("Login")
    with btn2 :
        if st.button("Register") :
            st.session_state.teacher = 'register'
            st.rerun()
def teacher_screen_register() :
    st.header('Register using password', text_alignment="center")

    teacher_name = st.text_input("User name", placeholder='Enter your full name')
    teacher_username = st.text_input("User name", placeholder='Enter your username')
    teacher_password = st.text_input("Password",type="password", placeholder='Enter your password')
    confirm_pass = st.text_input("Confirm Password",type="password", placeholder='Confirm your password')

    st.divider()

    btn1, btn2 = st.columns(2)
    with btn1 :
        st.button("Register")
    with btn2 :
        if st.button("Already have an account?") :
            st.session_state.teacher = "login"
            st.rerun()