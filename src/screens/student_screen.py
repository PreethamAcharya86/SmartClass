import streamlit as st
import numpy as np
from src.components.header import back
from PIL import Image

def student_screen() :
    back()
    st.header("Students Login!")

    img_source = st.camera_input("Possition your face in the center")
    if img_source :
        np.array(Image.open(img_source))
        