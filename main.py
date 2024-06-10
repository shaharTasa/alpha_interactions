import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import streamlit as st
import pandas as pd
import json

from json_analysis.get_alphafold_output import read_json_file

st.write("Alpha interactions detector")

full_data_json_file = read_json_file('C:\\Users\\shach\\Documents\\Alpha_interactions\\json_analysis\\json_output\\fold_Irrc75b_femnb1\\fold_lrrc75b_femnb1_full_data_0.json')
job_request = read_json_file('C:\\Users\\shach\\Documents\\Alpha_interactions\\json_analysis\\json_output\\fold_Irrc75b_femnb1\\fold_lrrc75b_femnb1_job_request.json')

