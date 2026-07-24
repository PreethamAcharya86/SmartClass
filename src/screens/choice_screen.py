import streamlit as st
#from src.components.header import back
from src.ui.base_layout import style_base_layout


def choice_screen() :
    style_base_layout()

    st.markdown(
        """
        <div style="text-align:center; margin:1rem 0 1.3rem;">
            <h2 style="margin:0; color:#1f376c;">Choose your role</h2>
            <p style="margin:0.35rem 0 0; color:#5b6b8a;">Pick the experience that fits you best.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="hero-card" style="text-align:center;">
                <h3 style="margin-top:0; color:#1f376c;">Student</h3>
                <p style="color:#51627e;">Join classes, view lessons, and stay on top of your learning.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Continue as Student", type='primary', use_container_width=True):
            st.session_state['login_type'] = "student"
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="hero-card" style="text-align:center;">
                <h3 style="margin-top:0; color:#1f376c;">Teacher</h3>
                <p style="color:#51627e;">Create lessons, manage students, and guide the class smoothly.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Continue as Teacher", type='primary', use_container_width=True):
            st.session_state['login_type'] = "teacher"
            st.rerun()