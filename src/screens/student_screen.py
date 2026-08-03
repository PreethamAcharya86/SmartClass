import streamlit as st
import numpy as np
from src.components.header import back, navbar
from src.pipelines.face_pipeline import predict_attendance, get_face_embedding, train_classifier
from src.components.subject_enroll_dialog import subject_enroll_dialog
from src.components.subject_card import subject_card
from src.components.unenroll_confirmation import unenroll_confirmation
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance
from PIL import Image
import time


def student_screen():
    navbar()
    back()

    show_registration = False

    if 'student_data' in st.session_state and st.session_state.user_role == 'student':
        student_dashboard()
        return

    st.markdown(
        """
        <div style="text-align:center; margin-bottom:1.2rem;">
            <div style="width:48px; height:48px; background:var(--blue-50); border-radius:50%; display:inline-flex; align-items:center; justify-content:center; margin-bottom:0.5rem;">
                <span class="material-symbols-outlined" style="color:var(--blue-600); font-size:26px;">photo_camera</span>
            </div>
            <h2 style="margin:0; color:var(--blue-900); font-size:1.6rem; font-weight:800;">Student Face Scan Login</h2>
            <p style="color:var(--gray-600); font-size:0.93rem; margin-top:0.3rem;">
                Position your face clearly in the camera frame to log in.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    img_source = st.camera_input("Position your face in the center of the frame")

    if img_source:
        img = np.array(Image.open(img_source))
        with st.spinner('Scanning face…'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning("No face detected. Please ensure good lighting and face the camera directly.")
            elif num_faces > 1:
                st.warning("Multiple faces detected. Please ensure only your face is in the frame.")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)
                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        time.sleep(1)
                        st.toast(f"Welcome back, {student['name']}!")
                        st.rerun()
                else:
                    st.info("Face not recognized. New student? Register below.")
                    show_registration = True

    if show_registration:
        _, mid_col, _ = st.columns([1, 2, 1])
        with mid_col:
            with st.container(border=True):
                st.markdown(
                    """
                    <div style="text-align:center; margin-bottom:1rem;">
                        <h3 style="margin:0; color:var(--blue-900); font-size:1.2rem;">New Student Registration</h3>
                        <p style="color:var(--gray-600); font-size:0.85rem; margin-top:0.2rem;">Enter your name to register your face.</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                new_name = st.text_input("Full Name", placeholder="Enter your full name")

                if st.button("Create Account", type="primary", use_container_width=True):
                    if new_name:
                        with st.spinner("Creating profile…"):
                            img = np.array(Image.open(img_source))
                            encodings = get_face_embedding(img)
                            if encodings:
                                face_emb = encodings[0].tolist()
                                response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=None)
                                if response_data:
                                    train_classifier()

                                    st.session_state.is_logged_in = True
                                    st.session_state.user_role = 'student'
                                    st.session_state.student_data = response_data[0]

                                    st.toast(f"Welcome, {new_name}!")
                                    time.sleep(1)
                                    st.rerun()
                                else:
                                    st.error("Could not capture face clearly. Please retake photo with clear lighting.")
                    else:
                        st.warning("Please enter your full name.")


def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data["student_id"]

    st.markdown(
        f"""
        <div style="margin-bottom:1rem;">
            <h2 style="margin:0; color:var(--blue-900);">Hello, {student_data['name']}</h2>
            <p style="color:var(--gray-600); margin:0.2rem 0 0; font-size:0.93rem;">Your enrolled subjects and attendance stats.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns([2, 1], vertical_alignment="center")
    with c1:
        st.subheader("My Subjects")
    with c2:
        if st.button("Enroll in Class", type="primary", use_container_width=True, icon=":material/add:"):
            subject_enroll_dialog()
    st.divider()

    with st.spinner("Loading subjects…"):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    if not subjects:
        st.markdown(
            """
            <div style="text-align:center; padding:2rem 1rem; color:var(--gray-600);">
                <p style="margin:0; font-size:1rem; font-weight:500;">You are not enrolled in any classes yet.</p>
                <p style="margin:0.3rem 0 0; font-size:0.88rem;">Click <strong>Enroll in Class</strong> above to join a subject.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    stats_map = {}
    for log in logs:
        sid = log["subject_id"]
        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}
        stats_map[sid]['total'] += 1
        if log.get("is_present"):
            stats_map[sid]['attended'] += 1

    cols = st.columns(2)

    for i, sub_node in enumerate(subjects):
        sub = sub_node["subjects"]
        id = sub["subject_id"]
        stats = stats_map.get(id, {"total": 0, "attended": 0})

        def unenroll_btn():
            if st.button("Unenroll", type="secondary", icon=":material/delete:", key=id):
                unenroll_confirmation(student_id, id)

        with cols[i % 2]:
            subject_card(
                sub["name"],
                sub["subject_code"],
                sub["section"],
                stats=[('📅', 'Total', stats['total']), ('✅', 'Attended', stats['attended'])],
                footer_callback=unenroll_btn
            )
