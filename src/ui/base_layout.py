import streamlit as st
import os

def style_base_layout():
    css_path = os.path.join(os.path.dirname(__file__), "styles.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css_lines = f.readlines()
    
    # Strip empty lines and comment lines to prevent Streamlit markdown parser from breaking out of <style>
    clean_css = []
    in_comment = False
    for line in css_lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("/*") and stripped.endswith("*/"):
            continue
        clean_css.append(line)
    
    css_content = "".join(clean_css)

    st.markdown(
        f"""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
        <style>
        {css_content}
        </style>
        """,
        unsafe_allow_html=True,
    )