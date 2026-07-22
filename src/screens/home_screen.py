import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout
from src.components.footer import footer
def home_screen() :
    header_home()

    style_base_layout()
    col1, col2 = st.columns(2)
    with col1 :
        if st.button("Student", type='primary', icon=':material/arrow_outward:',  icon_position='right') :
            st.session_state['login_type'] = "student"
            st.rerun()
    with col2 :
        if st.button("Teacher", type='primary', icon=':material/arrow_outward:', icon_position='right') :
            st.session_state['login_type'] = "teacher"
            st.rerun()
    footer()