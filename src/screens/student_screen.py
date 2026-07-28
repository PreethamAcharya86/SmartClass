import streamlit as st
import numpy as np
from src.components.header import back, navbar
from src.pipelines.face_pipeline import predict_attendance, get_face_embedding, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.components.subject_enroll_dialog import subject_enroll_dialog
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance
from PIL import Image
import time
def student_screen() :
    navbar()
    back()
    
    show_registration = False

    if 'student_data' in st.session_state and st.session_state.user_role == 'student':
        student_dashboard()

        return
    st.header("Students Login!")

    img_source = st.camera_input("Possition your face in the center")
    if img_source :
        img = np.array(Image.open(img_source))
        with st.spinner('AI is scanning') :
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0 : 
                st.warning("Face not found!")
            elif num_faces > 1 :
                st.warning("Multiple faces found!")
            else :
                if detected :
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)
                    if student :
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        time.sleep(1)
                        st.toast(f"Welcome back {student['name']}!")
                        st.rerun()
                else :
                    st.info("Face not recognised you might be a new student!")
                    show_registration = True
    if show_registration :
        with st.container(border=True) :
            st.header("Student Registration")
            new_name = st.text_input("Name", placeholder="Enter your name")
            st.subheader("Optional : Voice Enrollment")

            st.info("Enroll for voice only attendence")
            audio_data = None
            try :
                audio_data = st.audio_input("Record a short phrase of your voice!")
            except Exception :
                st.error('Audio data failed')
            if st.button("Create Account") :
                if new_name :
                    with st.spinner("Creating profile..") :
                        img = np.array(Image.open(img_source))
                        encodings = get_face_embedding(img)
                        if encodings :
                            face_emb = encodings[0].tolist()
                            voice_emb = None

                            if audio_data :
                                voice_emb = get_voice_embedding(audio_data.read())
                            response_data = create_student(new_name, face_embedding = face_emb, voice_embedding = voice_emb)
                            if response_data :
                                train_classifier()

                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]

                                st.toast(f"Welcome {new_name}")
                                time.sleep(1)
                                st.rerun()
                            else :
                                st.error("Coudn't able to capture facial recognisation")
                else :
                    st.warning("Pleace enter your name!")

def student_dashboard() :
    student_data = st.session_state.student_data
    student_id = student_data["student_id"]
    st.write(f"#### Hello {student_data['name']}")

    c1, c2 = st.columns(2)
    with c1 :
        st.subheader("Manage Subject")

    with c2 :
        if st.button("Enrol now", width="stretch") :
            subject_enroll_dialog() 
    st.divider()

    with st.spinner("Fetching subjects..") :
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    if subjects :
        for sub in subjects :
            print(sub["subject_id"])
        