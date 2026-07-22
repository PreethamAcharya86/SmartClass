import streamlit as st
def teacher_screen() :
    st.header("Teacher screen")

    if st.button("Back") :
        st.session_state["login_type"] = None
        st.rerun()