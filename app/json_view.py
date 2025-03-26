"""
Fjor Robles
"""
import streamlit as st
from data2 import web_scraper

st.markdown("# JSON View 🫘")
st.sidebar.markdown("# JSON View 🫘")

#point to the data file with the scraped information
data_file = "./app/data/menu.json" 
#call function
menu = web_scraper()

st.title("Strarbucks Menu data")
st.json(menu)
