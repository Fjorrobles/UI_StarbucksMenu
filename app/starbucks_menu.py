import streamlit as st
import json

# Path to the saved JSON data
data_file = "./app/data/menu.json"

def load_data():
    """Load data from the JSON file"""
    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error(f"File not found: {data_file}")
        return []
    except json.JSONDecodeError:
        st.error(f"Error decoding JSON data in: {data_file}")
        return []

st.markdown("# Starbucks Menu ☕️")
st.sidebar.markdown("# Starbucks Menu ☕️")
# Load the data from the JSON file
data = load_data()
# Check if there's data to display
if data:
    # Alternatively, if the data is just a list of items, you can display it as a table
    st.write("Menu Items:")
    st.dataframe(data)  # Display data as a table (if it's a list of dictionaries)
else:
    st.write("No data available to display.")
