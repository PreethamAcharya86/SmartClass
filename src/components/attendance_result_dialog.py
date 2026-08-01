import pandas
import streamlit as st

@st.dialog("Attendance result")
def attendance_result_dialog(df, logs) :
    st.write("Please review attendance before confirming")
    st.dataframe(df, hide_index=True, width="stretch")

    col1, col2 = st.columns(2)