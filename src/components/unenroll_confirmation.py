import streamlit as st
from src.database.db import unenroll_to_subject
import time

@st.dialog("Confirm Unenrollment")
def unenroll_confirmation(student_id, id) :
    st.write("Are you sure?")
    col1, col2 = st.columns(2)
    with col1 :
        if st.button("Confim", width="stretch") :
            unenroll_to_subject(student_id, id)
            st.toast("Unenrolled Successfully!")
            time.sleep(0.5)
            st.rerun()
    with col2 :
        if st.button("Cancel", type="primary", width="stretch") :
            st.rerun()
