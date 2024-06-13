import streamlit as st
import pandas as pd

def print_output(sequences_len, proteins_names, atom_plddts):
    st.write(f'input name: {proteins_names}')
    for i, seq_len in enumerate(sequences_len):
        st.write(f"Length of sequence {chr(65+i)}: {seq_len}")
    average_plddt = atom_plddts.sum() / len(atom_plddts)
    st.write(f'Average pLDDT: {average_plddt:.2f}')
    st.write("High-confidence inter-chain interactions :")
