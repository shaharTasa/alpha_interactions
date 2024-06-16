import streamlit as st

def checkbox_method(name,explain):
    chain_iptm_explain = st.checkbox(name)
    if chain_iptm_explain:
        st.info(explain, icon="ℹ️")
