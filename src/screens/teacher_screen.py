import streamlit as st
from src.components.header import back, navbar
from src.components.create_subject_dialog import create_subject_dialog
from src.components.share_subject_dialog import share_subject_dialog
from src.components.subject_card import subject_card
from src.components.take_attendance import take_attendance
from src.database.db import register_teacher, login_teacher, get_teacher_subjects
import time

def teacher_screen() :
    navbar()
    back()

    if 'teacher_data' in st.session_state and st.session_state.user_role == 'teacher':
        teacher_dashboard()
    elif 'teacher' not in st.session_state or st.session_state.teacher == "login" :
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


def teacher_dashboard() :
    data = st.session_state.teacher_data
    st.subheader(f"Hello {data['name']}!")

    if 'current_teacher_tab' not in st.session_state :
        st.session_state.current_teacher_tab = 'take_attendance'
    tab1, tab2, tab3 = st.columns(3)

    with tab1 :
        type = 'primary' if st.session_state.current_teacher_tab =='take_attendance' else 'secondary'
        if st.button("Take attendance", type = type, width='stretch', icon=':material/ar_on_you:') :
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()
    with tab2 :
        type = 'primary' if st.session_state.current_teacher_tab =='manage_subjects' else 'secondary'
        if st.button("Manage subjects", type=type, width='stretch', icon=':material/book_ribbon:') :
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()
    with tab3 :
        type = 'primary' if st.session_state.current_teacher_tab =='attendance_record' else 'secondary'
        if st.button("Attendance record",type=type, width='stretch', icon=':material/cards_stack:') :
            st.session_state.current_teacher_tab = 'attendance_record'
            st.rerun()
            
    st.divider()

    if st.session_state.current_teacher_tab =='take_attendance' :
        take_attendance()
    if st.session_state.current_teacher_tab =='manage_subjects' :
        manage_subjects(data)    
    if st.session_state.current_teacher_tab =='attendance_record' :
        attendance_record() 

def manage_subjects(data) :
    teacher_id = data['id']
    st.header("Subjects dashboard")  

    col1, col2 = st.columns(2)
    with col1 :
        st.subheader("Manage subjects")

    with col2 :
        if st.button("Create new Subject", width='stretch') :
            create_subject_dialog(teacher_id)

    subjects = get_teacher_subjects(teacher_id)
    
    if subjects :
        for subject in subjects :
            stats = [
                ("👨‍🎓","Students", subject["total_students"]),
                ("📚","Classes", subject["total_classes"])
            ]
            def share_btn() :
                if st.button(f"Share code:{subject['name']}", key=f"Share_{subject['subject_code']}", icon=":material/share:") :
                    share_subject_dialog(subject['name'], subject['subject_code'])
                    st.space()

            subject_card(
                name = subject['name'],
                code = subject['subject_code'],
                section = subject["section"],
                stats = stats,
                footer_callback = share_btn
            )

    else :
        st.info("No subject found!")

    
    

def attendance_record() :
    st.subheader("Attendance records")