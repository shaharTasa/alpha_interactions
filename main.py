import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import streamlit as st
import pandas as pd
import json
from json_analysis.json_process.utils.get_alphafold_output import read_json_file
from json_analysis.json_process.utils.extrect_data import extract_data_from_json
from json_analysis.interactions_analysis.find_intreactions import calculate_interactions
from json_analysis.interactions_analysis.print_interactions_results import print_output

st.logo('./assets/logo_protein.png')

st.image("./assets/alphafold_image.png")

st.title("_This_ is **Alpha fold interactions detector** ")
# st.subheader("instructions")
st.write("choose one of the options")
options = st.radio("Choose your data source:", ('Upload your own data', 'Use data from storage'))

if options == 'Upload your own data':
    st.write("upload here your output that you get from alphafold server https://alphafoldserver.com")
    selected_folder = st.file_uploader("Upload files that end with: **_full_data_0.json** and **_job_request.json**",accept_multiple_files=True)
           
else:
    data_storage_path = './assets/data_storage'
    if os.path.exists(data_storage_path) and os.path.isdir(data_storage_path):
        directories = [d for d in os.listdir(data_storage_path) if os.path.isdir(os.path.join(data_storage_path, d))]
    else:
        directories = []
    selected_folder = st.selectbox("Choose data", directories)
    st.write("You selected:", selected_folder)

if st.button("Perform Analysis"):
    if 
    folder_path = os.path.join(data_storage_path, selected_folder)
    files_in_selected_folder = os.listdir(folder_path)
    # st.write("Files in selected folder:", files_in_selected_folder)
    st.header("find interactions")

# data_load_state = st.text('Loading data...')



# sequences_len, sequences, proteins_names, full_pae, atom_plddts, contact_probs, token_chain_ids = extract_data_from_json(full_data_json_file, job_request)
# inter_chain_interactions = calculate_interactions(sequences, full_pae, contact_probs, token_chain_ids)
# df_interactions = pd.DataFrame(inter_chain_interactions,columns=['Chain_1','Residue_1','Position_1','Chain_2','Residue_2','Position_2','PAE','Probability'])
# print_output(sequences_len, proteins_names, atom_plddts)
# if st.checkbox('Show raw data'):
#     st.subheader('interactions')
#     st.write(df_interactions)

    
# st.write("Most objects") # df, err, func, keras!
# st.write(["st", "is <", 3]) # see *

# st.text("Fixed width text")
# st.markdown("_Markdown_") # see *
# st.latex(r""" e^{i\pi} + 1 = 0 """)
# st.title("My title")
# st.header("My header")
# st.subheader("My sub")



# col1, col2 = st.columns(2)
# col1.write("This is column 1")
# col2.write("This is column 2")

# # Three different columns:
# col1, col2, col3 = st.columns([3, 1, 1])
# # col1 is larger.

# # You can also use "with" notation:
# with col1:
#     st.radio("Select one:", [1, 2])
    

# st.checkbox("I agree")
# st.toggle("Enable")
# st.selectbox("Pick one", ["cats", "dogs"])
# st.multiselect("Buy", ["milk", "apples", "potatoes"])
# st.slider("Pick a number", 0, 100)
# st.select_slider("Pick a size", ["S", "M", "L"])
# st.text_input("First name")
# st.number_input("Pick a number", 0, 10)
# st.text_area("Text to translate")
# st.date_input("Your birthday")
# st.time_input("Meeting time")
# st.file_uploader("Upload a CSV")
# # st.camera_input("Take a picture")
# st.color_picker("Pick a color")
    
# if __name__ == "__main__":
#     mainpy()