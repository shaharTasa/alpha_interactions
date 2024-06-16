
import streamlit as st
import json
from data_analysis.json_process.utils.extrect_data import extract_data_from_full_data_json
import os
from data_analysis.best_model.output_best_model import get_best_model
from draws.tabs import tab1_data_protein,tab2_raw_data,tab3_plots,tab4_visual

    
def draw_output_data(folder_path):

    try:
        files = os.listdir(folder_path)
    except FileNotFoundError:
        st.error(f"The selected file path {folder_path} does not exist.")
        return
    
    sel_model_num = get_best_model(files,folder_path)
    
    full_data_pattern = f"_full_data_{sel_model_num}.json"
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
            extract_data_from_full_data_json(full_data_json, job_request_json)

    except Exception as e:
        st.error(f"Error during data extraction: {str(e)}")
        return
    
    
    tab1, tab2,tab3,tab4,tab5 = st.tabs([ "🗃 Data of the protein"," 📝 raw data","📈plots ","💊 visualization","📖output interpret"])
    tab1_data_protein(folder_path, files, sel_model_num, sequences_len, sequences, proteins_names, atom_plddts, tab1)
    df_interactions = tab2_raw_data(sequences, full_pae, contact_probs, token_chain_ids, tab2)
    tab3_plots(tab3, df_interactions)
    tab4_visual(folder_path, sel_model_num, tab4)   
    # tab5_inerpert(tab5)
