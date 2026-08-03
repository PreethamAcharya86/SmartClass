import streamlit as st
from src.ui.base_layout import style_base_layout


def choice_screen():
    style_base_layout()

    if st.button("Back", key='choice_back', icon=":material/arrow_back:"):
        st.session_state['login_type'] = None
        st.rerun()

    st.markdown(
        """
        <div style="text-align:center; margin:0.8rem 0 1.2rem;">
            <h2 style="margin:0; color:var(--blue-900); font-size:1.7rem; font-weight:800;">
                Choose Your Role
            </h2>
            <p style="margin:0.3rem 0 0; color:var(--gray-600); font-size:0.93rem;">
                Select your account type to proceed to your portal.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="role-card">
                <div class="role-icon-box">
                    <span class="material-symbols-outlined" style="font-size:30px;">school</span>
                </div>
                <h3>Student</h3>
                <p>Log in with face scan, enroll in subjects, and track your attendance progress.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Continue as Student", type='primary', use_container_width=True, icon=":material/school:"):
            st.session_state['login_type'] = "student"
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="role-card">
                <div class="role-icon-box">
                    <span class="material-symbols-outlined" style="font-size:30px;">person</span>
                </div>
                <h3>Teacher</h3>
                <p>Manage subject rosters, scan classroom photos, and generate attendance reports.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Continue as Teacher", type='primary', use_container_width=True, icon=":material/person:"):
            st.session_state['login_type'] = "teacher"
            st.rerun()