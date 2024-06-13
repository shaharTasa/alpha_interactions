import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import streamlit as st
import pandas as pd
import json
from json_analysis.json_process.utils.get_alphafold_output import read_json_file
from json_analysis.json_process.utils.extrect_data import extract_data_from_json
from json_analysis.interactions_analysis.find_intreactions import calculate_interactions
from json_analysis.interactions_analysis.print_interactions_results import print_output

st.logo('C:\\Users\\shach\\Documents\\Alpha_interactions\\json_analysis\\json_process\\utils\\Picture2.png')
st.image("C:\\Users\\shach\\Documents\\Alpha_interactions\\json_analysis\\json_process\\utils\\image1.png", width=500)

st.title("_This_ is **Alpha fold interactions detector** ")
st.subheader("instructions:")

st.write("1. First, upload here your output that you get from alphafold server https://alphafoldserver.com/about")
st.write("2. the require output is all the data that you can from the zip file here there is an example and you can change it")

g = st.file_uploader("Upload all the output",accept_multiple_files=True)

data_load_state = st.text('Loading data...')

full_data_json_file = read_json_file('C:\\Users\\shach\\Documents\\Alpha_interactions\\json_analysis\\json_process\\input_files\\fold_Irrc75b_femnb1\\fold_lrrc75b_femnb1_full_data_0.json')
job_request = read_json_file('C:\\Users\\shach\\Documents\\Alpha_interactions\\json_analysis\\json_process\\input_files\\fold_Irrc75b_femnb1\\fold_lrrc75b_femnb1_job_request.json')
st.header("find interactions")

sequences_len, sequences, proteins_names, full_pae, atom_plddts, contact_probs, token_chain_ids = extract_data_from_json(full_data_json_file, job_request)
inter_chain_interactions = calculate_interactions(sequences, full_pae, contact_probs, token_chain_ids)
df_interactions = pd.DataFrame(inter_chain_interactions,columns=['Chain_1','Residue_1','Position_1','Chain_2','Residue_2','Position_2','PAE','Probability'])
print_output(sequences_len, proteins_names, atom_plddts)
if st.checkbox('Show raw data'):
    st.subheader('interactions')
    st.write(df_interactions)

st.write("Most objects") # df, err, func, keras!
st.write(["st", "is <", 3]) # see *

st.text("Fixed width text")
st.markdown("_Markdown_") # see *
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")



col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

# Three different columns:
col1, col2, col3 = st.columns([3, 1, 1])
# col1 is larger.

# You can also use "with" notation:
with col1:
    st.radio("Select one:", [1, 2])
    

st.checkbox("I agree")
st.toggle("Enable")
st.radio("Pick one", ["cats", "dogs"])
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
# st.camera_input("Take a picture")
st.color_picker("Pick a color")
    
# if __name__ == "__main__":
#     mainpy()