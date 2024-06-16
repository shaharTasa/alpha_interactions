import streamlit as st

def checkbox_method(name,explain):
    # chain_iptm_explain = st.checkbox(name)
    st.markdown(name, help =explain)
