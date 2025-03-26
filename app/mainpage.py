"""
Fjor Robles
used Streamlit multipage website code as a start
"""
import streamlit as st

# Define the pages 
main_page = st.Page("starbucks_menu.py", title="Starbucks Menu", icon="☕️")
page_2 = st.Page("json_view.py", title="JSON View", icon="🫘")


# Set up navigation
pg = st.navigation([main_page, page_2])

# Run the selected page
pg.run()
