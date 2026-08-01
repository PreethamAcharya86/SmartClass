import streamlit as st
from src.database.db import get_attendance_for_teacher
from datetime import datetime
import pandas as pd

def attendance_record() :
    st.subheader("Attendance records")
    teacher_id = st.session_state.teacher_data["id"]
    records = get_attendance_for_teacher(teacher_id)

    if not records :
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWGqo_db2tW-auSmOvGxqRUUuachAf1h_GIbbSKjnj5Cn-AL-n7b_kD94&s=10", width=300)
        st.info("No records found!")
        return
    data = []
    for record in records :
        ts = record["timestamp"]

        data.append({
            "ts_group" : ts.split(".")[0] if ts else None,
            "Time" : datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "NA",
            "Subject" : record["subjects"]["name"],
            "Subject Code" : record["subjects"]["subject_code"],
            "is_present" : bool(record.get("is_present", False))
        })

        

    df = pd.DataFrame(data)
        
    summary = (
    df.groupby(["ts_group", "Time", "Subject", "Subject Code"])
      .agg(
          Present_Count=("is_present", "sum"),
          Total_Count=("is_present", "count")
      )
      .reset_index()
    )

    summary["Absent_Count"] = (
        summary["Total_Count"] - summary["Present_Count"]
    )

    summary["Attendance Status"] = (
        "✅Present: "
        + summary["Present_Count"].astype(str)
        + " |❌Absent: "
        + summary["Absent_Count"].astype(str)
        + " | Total: "
        + summary["Total_Count"].astype(str)
    )
    display_df = ( summary.sort_values(by="ts_group", ascending=False)
                  [["Time", "Subject", "Subject Code", "Attendance Status"]]
    )
    st.dataframe(display_df, width="stretch", hide_index=True, column_config={
        "Time": st.column_config.TextColumn(width="small"),
        "Subject": st.column_config.TextColumn(width="small"),
        "Subject Code": st.column_config.TextColumn(width="small"),
        "Attendance Status": st.column_config.TextColumn(width="medium"),
    },)
