import streamlit as st
def style_base_layout() :
    st.markdown(
        """
            <style> 
                #MainMenu, header, footer {
                    visibility : hidden; 
                } 
            </style>
        """
    , unsafe_allow_html=True)