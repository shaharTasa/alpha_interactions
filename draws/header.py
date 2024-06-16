import streamlit as st

def draw_header():
    col1,col2=st.columns([20,100])
    col2.title("_This_ is **Alpha fold interactions detector** ")
    col1.image('./assets/protein.png')
