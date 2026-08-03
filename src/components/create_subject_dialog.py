import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.markdown("Fill in the details for your new subject.")
    sub_id = st.text_input("Subject Code", placeholder="e.g. CS101")
    sub_name = st.text_input("Subject Name", placeholder="e.g. Computer Science")
    sub_section = st.text_input("Section", placeholder="e.g. A")

    if st.button("Create Subject", type="primary", width="stretch"):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast("Subject created successfully!")
                st.rerun()
            except Exception:
                st.error("Something went wrong. Please check your subject code and try again.")
        else:
            st.warning("Please fill in all fields before continuing.")