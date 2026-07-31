import streamlit as st
from src.database.db import get_teacher_subjects

def take_attendance() :
    teacher_data = st.session_state.teacher_data
    teacher_id = teacher_data["id"]
    st.subheader("Take Attendance") 

    if 'attendance_images' not in st.session_state :
        st.session_state.attendance_images = []

    subjects = get_teacher_subjects(teacher_id)

    if not subjects :
        st.info("You haven't created any subjects. Please create one to begin!")
        return
    subject_options = {f"{s["name"]} : {s["subject_code"]}" : s["subject_id"] for s in subjects}


    col1, col2 = st.columns([3, 1])
    with col1 :
        selected_subject = st.selectbox("Select Subject", options=list(subject_options.keys()))