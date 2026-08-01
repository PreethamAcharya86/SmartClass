import streamlit as st
from PIL import Image
import time

@st.dialog("Add photos")
def add_photo_dialog() :
    st.write("Add classroom photo")

    if "photo_tab" not in st.session_state :
        st.session_state.photo_tab = "camera"

    t1, t2 = st.columns(2)
    with t1 :
        if st.button("Open Camera", width="stretch", type="primary") :
            st.session_state.photo_tab = "camera"

    with t2 :
        if st.button("Upload Photo", width="stretch") :
            st.session_state.photo_tab = "upload"

    if st.session_state.photo_tab == "camera" :
        cam_photo = st.camera_input("Take classroom photo", key="camera")

        if cam_photo :
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast("Photo captured!")
            time.sleep(0.5)
            st.rerun()

    if st.session_state.photo_tab == "upload" :
            uploaded_files = st.file_uploader("Choose image files", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key='upload')

            if uploaded_files :
                for img in uploaded_files :
                    st.session_state.attendance_images.append(Image.open(img))
                st.toast("Photos uploaded!")
                time.sleep(0.5)
                st.rerun()

    if st.button("Done", width="stretch") :
        st.rerun()
            