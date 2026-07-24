import streamlit as st
from src.components.header import header_home, navbar
from src.ui.base_layout import style_base_layout
from src.components.footer import footer


def home_screen() :
    style_base_layout()
    navbar()
    header_home()

    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([1.15, 0.85])

    with col1:
        st.markdown(
            """
            <h2 style="color:#1f376c; margin-bottom:0.35rem;">Create a brighter classroom experience</h2>
            <p style="color:#51627e; font-size:1.02rem; line-height:1.6;">
                Welcome to Smart Class — a polished learning hub where teachers can guide lessons and students can jump into their workspace with ease.
            </p>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Start learning", type="primary"):
            st.session_state['login_type'] = 'choose'
            st.rerun()

    #with col2:
        #st.image(hero_path, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.divider()
    footer()