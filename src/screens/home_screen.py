import base64
from pathlib import Path

import streamlit as st
from src.components.header import navbar
from src.ui.base_layout import style_base_layout
from src.components.footer import footer


def _render_image_card(image_filename: str, alt_text: str, width: int = 420):
    image_path = Path(__file__).resolve().parents[1] / "Images" / image_filename
    with image_path.open("rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("ascii")

    st.markdown(
        f"""
        <div class="hero-visual-card">
            <img src="data:image/png;base64,{encoded_image}" alt="{alt_text}" style="max-width:{width}px;" />
        </div>
        """,
        unsafe_allow_html=True,
    )


def home_screen():
    style_base_layout()
    navbar()

    col1, col2 = st.columns([1.15, 0.85], vertical_alignment="center")

    with col1:
        st.markdown(
            """
            <div class="hero-card">
                <div class="hero-badge">AI-powered attendance</div>
                <h2>Automate Attendance with AI Face Recognition</h2>
                <p>
                    Welcome to <strong>VisualAttend</strong> — a polished, fast classroom attendance experience designed for modern schools.
                    Teachers can scan classroom photos in seconds, and students gain instant visibility into their attendance performance.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Get Started", type="primary", icon=":material/arrow_forward:"):
            st.session_state['login_type'] = 'choose'
            st.rerun()

    with col2:
        _render_image_card("hero_section.png", "VisualAttend hero illustration", width=460)
        st.markdown(
            """
            <div class="hero-note-card">
                <h4>Built for fast, modern classrooms</h4>
                <p>From instant face-based sign-in to cleaner attendance insights, every detail is designed to feel effortless.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

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