import streamlit as st
import segno
import io

@st.dialog("Share Class Link")
def share_subject_dialog(sub_name, sub_code):
    st.markdown(f"Share link or QR code for **{sub_name}**.")
    app_domain = "visualattend.streamlit.app"
    join_url = f"{app_domain}/?join-code={sub_code}"

    qr = segno.make(join_url)

    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Copy Link")
        st.code(join_url, language='text', width="stretch")
        st.markdown("#### Class Code")
        st.code(sub_code, language="text")
        st.info("Share this link or code with your students to let them join.")

    with col2:
        st.markdown("#### Scan to Join")
        st.image(out.getvalue(), caption="QR Code")