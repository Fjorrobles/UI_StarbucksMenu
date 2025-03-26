import streamlit as st
from data2 import web_scraper

st.markdown("# JSON View 🫘")
st.sidebar.markdown("# JSON View 🫘")

data_file = "./app/data/menu.json" 
menu = web_scraper()

st.title("Strarbucks Menu data")
st.json(menu)
