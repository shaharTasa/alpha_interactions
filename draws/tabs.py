import streamlit as st
import pandas as pd
from data_analysis.interactions_analysis.find_intreactions import calculate_interactions
from data_analysis.interactions_analysis.print_interactions_results import print_output
from data_analysis.interactions_analysis.plot_interactions import create_scatter_plot,visualization_protein
from data_analysis.interactions_analysis.output_script_for_chimerax import writing_commends_to_file_and_create_button
import glob
import os

def tab4_visual(folder_path, sel_model_num, tab4):
    with tab4:
        pattern = f"*_model_{sel_model_num}.cif"
        found_files = glob.glob(os.path.join(folder_path, pattern))
        tab4.subheader('CIF File Viewer for Protein Models')
        if found_files:
            visualization_protein(found_files)
        else:
            st.write("No CIF files found.")       
def tab3_plots(tab3, df_interactions):
    heatmap_fig = create_scatter_plot(df_interactions)
    tab3.plotly_chart(heatmap_fig)

def tab2_raw_data(sequences, full_pae, contact_probs, token_chain_ids, tab2):
    with tab2:
        tab2.subheader('Interactions between protein A to B')
        st.markdown("""
        Below is the table detailing inter-chain interactions:
        - **Probability**: The predicted probability that token i and token j are in contact (8Å between the representative atom for each token).
        - **PAE**: Positional error estimate between predicted and true positions.
        """)
        pae_threshold = tab2.slider('Select PAE Threshold', min_value=0.0, max_value=max(full_pae.flatten()), value=max(full_pae.flatten())/2, step=0.1)
        contact_prob_threshold = tab2.slider('Select Contact Probability Threshold', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        inter_chain_interactions = calculate_interactions(sequences, full_pae, contact_probs, token_chain_ids,pae_threshold ,contact_prob_threshold)
        df_interactions = pd.DataFrame(inter_chain_interactions,columns=['Chain_1','Residue_1','Position_1','Chain_2','Residue_2','Position_2','PAE','Probability']).sort_values(by='Probability', ascending=False)
        tab2.info('Notice : **low PAE** and **high Probability** means high probability of connection . ', icon="ℹ️")
        tab2.write(df_interactions)
        writing_commends_to_file_and_create_button(inter_chain_interactions)

    return df_interactions

def tab1_data_protein(folder_path, files, sel_model_num, sequences_len, sequences, proteins_names, atom_plddts, tab1):
    with tab1:
        summery_pattern = f"_summary_confidences_{sel_model_num}.json"
        job_summery_files = [file for file in files if file.endswith(summery_pattern)]
        st.subheader("Proteins details")
        print_output(tab1,sequences,sequences_len, proteins_names, atom_plddts,job_summery_files[0],folder_path)



# def tab5_inerpert(tab5):
#     with tab5:
#         st.markdown(':petri_dish: \t :blue-background[pLDDT]: a per-atom confidence estimate on a 0-100 scale where a higher value indicates higher confidence.\n')
#         st.markdown(':petri_dish: \t :blue-background[PAE (predicted aligned error)]: estimate of the error in the relative position and orientation between two tokens in the predicted structure. Higher values indicate higher predicted error and therefore lower confidence\n')
#         st.markdown(':petri_dish: \t :blue-background[ptm]: A scalar in the range 0-1 indicating the predicted TM-score for the full structure.\n')
#         st.markdown(':petri_dish: \t :blue-background[iptm]: A scalar in the range 0-1 indicating predicted interface TM-score (confidence in the predicted interfaces) for all interfaces in the structure.\n')
#         st.markdown(':petri_dish: \t :blue-background[fraction_disordered]: A scalar in the range 0-1 that indicates what fraction of the prediction structure is disordered, as measured by accessible surface area.\n')
#         st.markdown(':petri_dish: \t :blue-background[has_clash]:  A boolean indicating if the structure has a significant number of clashing atoms (more than 50% of a chain, or a chain with more than 100 clashing atoms)..\n')
#         st.markdown(':petri_dish: \t :blue-background[ranking_score] : A scalar in the range [-100, 1.5] that can be used for ranking predictions.\n')
#         st.code('0.8 × ipTM + 0.2 × pTM + 0.5 × disorder − 100 × has_clash')

