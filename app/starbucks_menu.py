from data import open_webpage
import streamlit as st

st.title="Starbucks Menu☕️",
#st.title="☕️",
logo = "https://www.citypng.com/photo/13466/hd-starbucks-text-logo-png"
st.image(logo,caption="Logo")

st.markdown(
    """
    <style>
        header { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)
menu = open_webpage()

url_logo = "https://www.citypng.com/photo/13466/hd-starbucks-text-logo-png"
st.image(url_logo)