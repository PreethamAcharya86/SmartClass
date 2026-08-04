import base64
from pathlib import Path

import streamlit as st
from src.ui.base_layout import style_base_layout


def _render_role_card(filename: str, title: str, description: str):
    image_path = Path(__file__).resolve().parents[1] / "Images" / filename

    with image_path.open("rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("ascii")

    st.markdown(
        f"""
        <div class="role-card role-card--select">
            <img src="data:image/png;base64,{encoded_image}" alt="{title}" />
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def choice_screen():
    style_base_layout()

    if st.button("Back", key='choice_back', icon=":material/arrow_back:"):
        st.session_state['login_type'] = None
        st.rerun()

    st.markdown(
        """
        <div class="choice-hero">
            <h2>Choose Your Role</h2>
            <p>Select your account type to continue to your portal.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        _render_role_card(
            "studentIcon.png",
            "Student",
            "Log in with face scan, enroll in subjects, and track your attendance progress.",
        )
        if st.button("Continue as Student", type='primary', use_container_width=True, icon=":material/school:"):
            st.session_state['login_type'] = "student"
            st.rerun()

    with col2:
        _render_role_card(
            "teacherIcon.png",
            "Teacher",
            "Manage subject rosters, scan classroom photos, and generate attendance reports.",
        )
        if st.button("Continue as Teacher", type='primary', use_container_width=True, icon=":material/person:"):
            st.session_state['login_type'] = "teacher"
            st.rerun()