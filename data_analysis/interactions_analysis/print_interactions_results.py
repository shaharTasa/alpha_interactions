import streamlit as st
import pandas as pd
from draws.check_method import checkbox_method
from data_analysis.json_process.utils.extrect_data import extract_data_from_summary

def print_output(tab1,sequences, sequences_len, proteins_names, atom_plddts,job_summery_files,folder_path):
    with tab1:
        st.write(f'**Input name:** {proteins_names}')
        average_plddt = atom_plddts.mean()
        checkbox_method(f'**Average pLDDT**: {average_plddt:.2f}','a per-atom confidence estimate on a 0-100 scale where a higher value indicates higher confidence. pLDDT aims to predict a modified LDDT score that only considers distances to polymers.')
        extract_data_from_summary(job_summery_files,folder_path)

        for i, seq_len in enumerate(sequences_len):
            with st.expander(f'Sequence {chr(65+i)}'):
                st.write(f"Length of sequence {chr(65+i)}: {seq_len}")
                st.write(f"Sequence: {sequences[i]}")
        


