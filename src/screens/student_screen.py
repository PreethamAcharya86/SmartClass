import streamlit as st
def student_screen() :
    st.header("Students")

    if st.button("Back") :
        st.session_state["login_type"] = None
        st.rerun()