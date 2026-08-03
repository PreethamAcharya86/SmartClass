import streamlit as st

def footer():
    st.markdown(
        """
        <div class="va-footer">
            <p>VisualAttend &nbsp;·&nbsp; AI-Powered Attendance System</p>
            <p style="margin-top:0.3rem;">
                Contact: <a href="mailto:preethamacharya16@gmail.com">preethamacharya16@gmail.com</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )