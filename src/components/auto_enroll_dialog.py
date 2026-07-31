import streamlit as st
from src.database.config import supabase
from src.database.db import enroll_to_subject
import time

@st.dialog("Enroll to class")
def auto_enroll_dialog(join_code) :
    student_data = st.session_state.student_data
    col1, col2 = st.columns(2)

    with col1 :
        if st.button("Enroll now") :
            if join_code :
                res = supabase.table("subjects").select("subject_id, name, subject_code").eq("subject_code", join_code).execute()
                if res.data :
                    subject = res.data[0]
                    student_id = student_data["student_id"]
                
                    check = supabase.table("subject_students").select("*").eq('subject_id', subject["subject_id"]).eq("student_id", student_id).execute()
                
                    if check.data :
                        st.info("You are already enrolled!")
                        time.sleep(1)
                        st.rerun()
                    else :
                        try :
                            enroll_to_subject(student_id, subject['subject_id'])
                            st.toast("Successfully enrolled")
                            time.sleep(1)
                            st.query_params.clear()
                            st.rerun()
                        except Exception as e :
                            st.error(f"Error : Unable to enroll please try again!")
                else :
                    st.warning("Wrong code check further!")
    with col2 :
        if st.button("No thanks") :
            st.query_params.clear()
            st.rerun()