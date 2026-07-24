import streamlit as st
from src.screens.choice_screen import choice_screen 

def header_home() :
    st.header("SMART CLASS", text_alignment="center")

def navbar() :
    c1, c2 = st.columns(2)
    with c1 :
        st.write("SMART CLASS")
    with c2 :
        if st.button("Get started") :
            st.session_state['login_type'] = 'choose'
            st.rerun()
        

def back() :
    if st.button('<--') :
        st.session_state['login_type'] = None
        st.rerun()
