import streamlit as st
import pandas as pd

def print_output(tab1,sequences, sequences_len, proteins_names, atom_plddts):
    with tab1:
        st.write(f'**Input name:** {proteins_names}')
        for i, seq_len in enumerate(sequences_len):
            with st.expander(f'Sequence {chr(65+i)}'):
                st.write(f"Length of sequence {chr(65+i)}: {seq_len}")
                st.write(f"Sequence: {sequences[i]}")
        
        average_plddt = atom_plddts.mean()
        st.write(f'**Average pLDDT**: {average_plddt:.2f}')


