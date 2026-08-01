import streamlit as st
import segno
import io

@st.dialog("Share class link")
def share_subject_dialog(sub_name, sub_code) :
    st.write(f"Link to {sub_name}")
    app_domain = "visualattend-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={sub_code}"

    qr = segno.make(join_url)

    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)
    with col1 :
        st.markdown("### Copy link")
        st.code(join_url, language='text', width="stretch")
        st.code(sub_code, language="text")
        st.info('Copy this link to share class code')

    with col2 :
        st.markdown("### Scan to join")
        st.image(out.getvalue(), caption="QR code to join class")