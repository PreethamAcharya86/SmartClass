import pandas
import streamlit as st
from src.database.db import create_attendance

@st.dialog("Attendance Result")
def attendance_result_dialog(df, logs):
    st.markdown("Please review attendance before confirming.")
    st.dataframe(df, hide_index=True, width="stretch")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Discard", width="stretch"):
            st.rerun()

    with col2:
        if st.button("Confirm & Save", type="primary", width="stretch"):
            try:
                create_attendance(logs)
                st.toast("Attendance saved successfully!")
                st.session_state.attendance_images = []
                st.rerun()
            except Exception:
                st.error("Failed to save attendance. Please try again.")
