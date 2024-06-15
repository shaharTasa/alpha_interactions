import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import streamlit as st
import pandas as pd
import json
from json_analysis.json_process.utils.extrect_data import extract_data_from_json
from json_analysis.interactions_analysis.find_intreactions import calculate_interactions
from json_analysis.interactions_analysis.print_interactions_results import print_output


def draw_output_data(folder_path):

    try:
        files = os.listdir(folder_path)
    except FileNotFoundError:
        st.error(f"The selected file path {folder_path} does not exist.")
        return

    model_number = st.number_input("Enter the model number:", min_value=0, value=0, step=1)
    full_data_pattern = f"_full_data_{model_number}.json"
    job_request_pattern = "_job_request.json"
    full_data_files = [file for file in files if file.endswith(full_data_pattern)]
    job_request_files = [file for file in files if file.endswith(job_request_pattern)]

    if not full_data_files:
        st.error("The selected model data file does not exist. Please check the model number.")
        return
    if not job_request_files:
        st.error("Job request file does not exist.")
        return

    full_data_json_path = os.path.join(folder_path, full_data_files[0])
    job_request_path = os.path.join(folder_path, job_request_files[0])

    try:
        with open(full_data_json_path, 'r') as file:
            full_data_json = json.load(file)
        with open(job_request_path, 'r') as file:
            job_request_json = json.load(file)
    except Exception as e:
        st.error(f"Failed to load or parse the JSON file: {str(e)}")
        return

    try:
        sequences_len, sequences, proteins_names, full_pae, atom_plddts, contact_probs, token_chain_ids  = \
            extract_data_from_json(full_data_json, job_request_json)

    except Exception as e:
        st.error(f"Error during data extraction: {str(e)}")
        return
    
    tab1, tab2 = st.tabs([ "🗃 Data of the protein","📈 row data"])
    print_output(tab1,sequences,sequences_len, proteins_names, atom_plddts)
    
    pae_threshold = tab2.slider('Select PAE Threshold', min_value=0.0, max_value=31.29, value=5.0, step=0.1)
    contact_prob_threshold = tab2.slider('Select Contact Probability Threshold', min_value=0.0, max_value=1.0, value=0.7, step=0.01)
    inter_chain_interactions = calculate_interactions(sequences, full_pae, contact_probs, token_chain_ids,pae_threshold ,contact_prob_threshold)
    df_interactions = pd.DataFrame(inter_chain_interactions,columns=['Chain_1','Residue_1','Position_1','Chain_2','Residue_2','Position_2','PAE','Probability'])
    tab2.subheader('Interactions between protein A to B')
    tab2.write(df_interactions)
    