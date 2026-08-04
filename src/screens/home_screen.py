import streamlit as st
from src.components.header import navbar
from src.ui.base_layout import style_base_layout
from src.components.footer import footer


def home_screen():
    style_base_layout()
    navbar()

    col1, col2 = st.columns([1.3, 0.7], vertical_alignment="center")

    with col1:
        st.markdown(
            """
            <div class="hero-card">
                <h2>Automate Attendance with AI Face Recognition</h2>
                <p>
                    Welcome to <strong>VisualAttend</strong> — a modern, fast classroom attendance system.
                    Teachers can scan classroom photos in seconds, and students get instant visibility into their attendance performance.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Get Started", type="primary", icon=":material/arrow_forward:"):
            st.session_state['login_type'] = 'choose'
            st.rerun()

    with col2:
        st.image("src/Images/Project_icon.png", width=400)

    st.markdown(
        """
        <div class="feature-row">
            <div class="feature-card">
                <div class="fc-icon-box">
                    <span class="material-symbols-outlined">face</span>
                </div>
                <h4>AI Face Recognition</h4>
                <p>Detect and mark student attendance automatically using computer vision technology.</p>
            </div>
            <div class="feature-card">
                <div class="fc-icon-box">
                    <span class="material-symbols-outlined">analytics</span>
                </div>
                <h4>Instant Insights</h4>
                <p>Track real-time subject stats, attendance percentages, and detailed logs.</p>
            </div>
            <div class="feature-card">
                <div class="fc-icon-box">
                    <span class="material-symbols-outlined">qr_code_scanner</span>
                </div>
                <h4>Easy Class Enrollment</h4>
                <p>Students join classes instantly via unique subject codes or QR code scanning.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    footer()