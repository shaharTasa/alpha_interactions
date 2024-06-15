import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import streamlit as st
import pandas as pd
import json
from json_analysis.json_process.utils.get_alphafold_output import read_json_file
from json_analysis.json_process.utils.extrect_data import extract_data_from_json
from json_analysis.interactions_analysis.find_intreactions import calculate_interactions
from json_analysis.interactions_analysis.print_interactions_results import print_output
import numpy as np
import zipfile


DATA_STORAGE_PATH = './assets/data_storage'

# Initialize Application
def init_app():
    st.image('./assets/logo_protein.png')
    st.title("_This_ is **Alpha fold interactions detector** ")
    options = st.radio("Choose your data source:", ('Upload your own data', 'Use data from storage'))
    return options


def handle_file_uploads():
    st.write("Upload the ZIP file that contains the output from the AlphaFold server: https://alphafoldserver.com")
    uploaded_file = st.file_uploader("Upload the ZIP file containing all the files", type=['zip'])

    if uploaded_file is not None:
        # Create a temporary directory to extract the zip file
        with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
            # Create a folder name from the zip file name
            folder_name = os.path.splitext(uploaded_file.name)[0]
            new_folder_path = os.path.join(DATA_STORAGE_PATH, folder_name)
            os.makedirs(new_folder_path, exist_ok=True)
            
            # Extract all the files into the directory
            zip_ref.extractall(new_folder_path)

        st.success(f"Files uploaded and saved successfully in folder: {new_folder_path}")
        return new_folder_path
    else:
        st.error("Please upload a zip file.")
    return None

def perform_data_analysis(folder_path):
    # Combine base data storage path with the selected folder name

    # Check if folder path exists
    if not os.path.exists(folder_path):
        st.error("The specified folder does not exist.")
        return

    # List all files in the directory
    try:
        files = os.listdir(folder_path)
    except FileNotFoundError:
        st.error(f"The folder path {folder_path} does not exist.")
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
        pae_threshold = st.slider('Select PAE Threshold', min_value=0.0, max_value=31.29, value=5.0, step=0.1)
        contact_prob_threshold = st.slider('Select Contact Probability Threshold', min_value=0.0, max_value=1.0, value=0.7, step=0.01)
 
        inter_chain_interactions = calculate_interactions(sequences, full_pae, contact_probs, token_chain_ids,pae_threshold ,contact_prob_threshold)
        df_interactions = pd.DataFrame(inter_chain_interactions,columns=['Chain_1','Residue_1','Position_1','Chain_2','Residue_2','Position_2','PAE','Probability'])
    except Exception as e:
        st.error(f"Error during data extraction: {str(e)}")
        return

    print_output(sequences_len, proteins_names, atom_plddts)
    
    if st.checkbox('Show raw data'):
        st.subheader('Interactions between protein A to B')
        st.write(df_interactions)
    

# Main Execution Flow
if __name__ == "__main__":
    options = init_app()

    if options == 'Upload your own data':
        selected_folder = handle_file_uploads()
    else:
        if os.path.exists(DATA_STORAGE_PATH) and os.path.isdir(DATA_STORAGE_PATH):
            directories = [d for d in os.listdir(DATA_STORAGE_PATH) if os.path.isdir(os.path.join(DATA_STORAGE_PATH, d))]
            path_folder = st.selectbox("Choose data", directories)
            selected_folder = os.path.join(DATA_STORAGE_PATH, path_folder)

    
    if selected_folder:
        perform_data_analysis(selected_folder)