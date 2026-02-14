import streamlit as st
from pathlib import Path

st.set_page_config(page_title="For Rekha ❤️", layout="wide")

# Read the HTML file
html_content = Path("valentine.html").read_text()

# Display it
st.components.v1.html(html_content, height=2000, scrolling=True)
