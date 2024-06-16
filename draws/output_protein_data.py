import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import streamlit as st
import pandas as pd
import json
from json_analysis.json_process.utils.extrect_data import extract_data_from_json
from json_analysis.interactions_analysis.find_intreactions import calculate_interactions
from json_analysis.interactions_analysis.print_interactions_results import print_output
from json_analysis.interactions_analysis.plot_interactions import create_scatter_plot,visualization_protein
import glob


def draw_output_data(folder_path):

    try:
        files = os.listdir(folder_path)
    except FileNotFoundError:
        st.error(f"The selected file path {folder_path} does not exist.")
        return

    # model_number = st.number_input("select model number:", min_value=0, value=0, step=1)
    model_number=0
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
    tab1, tab2,tab3,tab4,tab5 = st.tabs([ "🗃 Data of the protein"," 📝 raw data","📈plots ","💊 visualization","📖output interpret"])

    
    
    print_output(tab1,sequences,sequences_len, proteins_names, atom_plddts)
    
    pae_threshold = tab2.slider('Select PAE Threshold', min_value=0.0, max_value=max(full_pae.flatten()), value=max(full_pae.flatten())/2, step=0.1)
    contact_prob_threshold = tab2.slider('Select Contact Probability Threshold', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    inter_chain_interactions = calculate_interactions(sequences, full_pae, contact_probs, token_chain_ids,pae_threshold ,contact_prob_threshold)
    df_interactions = pd.DataFrame(inter_chain_interactions,columns=['Chain_1','Residue_1','Position_1','Chain_2','Residue_2','Position_2','PAE','Probability']).sort_values(by='Probability', ascending=False)
    tab2.subheader('Interactions between protein A to B')
    tab2.info('Notice : **low PAE** and **high Probability** means high probability of connection . ', icon="ℹ️")
    tab2.write(df_interactions)

    heatmap_fig = create_scatter_plot(df_interactions)
    tab3.plotly_chart(heatmap_fig)
    

    
    with tab4:
        pattern = f"*_model_{model_number}.cif"
        found_files = glob.glob(os.path.join(folder_path, pattern))
        tab4.title('CIF File Viewer for Protein Models')
        visualization_protein(found_files)
    with tab5:
        st.markdown(':petri_dish: \t :blue-background[pLDDT]: a per-atom confidence estimate on a 0-100 scale where a higher value indicates higher confidence.\n')
        st.markdown(':petri_dish: \t :blue-background[PAE (predicted aligned error)]: estimate of the error in the relative position and orientation between two tokens in the predicted structure. Higher values indicate higher predicted error and therefore lower confidence\n')
        st.markdown(':petri_dish: \t :blue-background[ptm]: A scalar in the range 0-1 indicating the predicted TM-score for the full structure.\n')
        st.markdown(':petri_dish: \t :blue-background[iptm]: A scalar in the range 0-1 indicating predicted interface TM-score (confidence in the predicted interfaces) for all interfaces in the structure.\n')
