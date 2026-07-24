import streamlit as st
from src.components.header import back
from src.database.db import register_teacher
from src.database.db import login_teacher
import time

def teacher_screen() :
    back()

    if 'teacher_data' in st.session_state :
        teacher_dashboard()
    elif 'teacher' not in st.session_state or st.session_state.teacher == "login" :
        teacher_screen_login()
    elif st.session_state.teacher == "register" :
        teacher_screen_register()

def teacher_dashboard() :
    data = st.session_state.teacher_data
    st.header(f"Hello {data['name']}!")

def teacher_screen_login() :
    st.header('Login using password', text_alignment="center")

    teacher_username = st.text_input("User name", placeholder='Enter your username')
    teacher_password = st.text_input("Password",type="password", placeholder='Enter your password')

    st.divider()

    btn1, btn2 = st.columns(2)
    with btn1 :
        if st.button("Login", shortcut='enter') :
            success, message =  login_teacher(teacher_username, teacher_password)
            if success :
                st.toast(message)
                time.sleep(1)
                st.rerun()
            else :
                st.error(message)
    with btn2 :
        if st.button("Register") :
            st.session_state.teacher = 'register'
            st.rerun()

def teacher_screen_register() :
    st.header('Register using password', text_alignment="center")

    teacher_name = st.text_input("User name", placeholder='Enter your full name')
    teacher_username = st.text_input("User name", placeholder='Enter your username')
    teacher_password = st.text_input("Password",type="password", placeholder='Enter your password')

    st.divider()

    btn1, btn2 = st.columns(2)
    with btn1 :
        if st.button("Register", shortcut="enter") :
            success, message =  register_teacher(teacher_name, teacher_username, teacher_password)
            if success :
                st.success(message)
                time.sleep(2)
                st.session_state.teacher = 'login'
                st.rerun()
            else :
                st.error(message)
                time.sleep(2)
            
    with btn2 :
        if st.button("Already have an account?") :
            st.session_state.teacher = "login"
            st.rerun()