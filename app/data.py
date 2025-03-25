from requests import get
from json import loads
from bs4 import BeautifulSoup
import streamlit as st

def open_webpage()-> dict:
    url = "https://www.starbucks.com/menu"
    try:
        menu = get(url)
        if menu.status_code == 200:
            soup = BeautifulSoup(menu.content,'html.parser')
            data = []
            menu_items = soup.find_all('div', class_='menu-item-class')
            for items in menu_items:
                data.append(items.get_text())
            return data
        else:
            st.error("Failed to retrieve data from webpage.")
            return{}
    except IOError as e:
        st.error(f"Error Occured: {e}")
    return {}



