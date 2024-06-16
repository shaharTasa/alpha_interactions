import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import streamlit as st
from json_analysis.best_model.model_number import get_model_number
import json
import os
import re

def get_best_model(files,folder_path):
    summery_pattern = r".*_summary_confidences_(\d)\.json"
    summery_data_files = [file for file in files if re.match(summery_pattern, file)]

    ranking_score={}
    
    for file in summery_data_files:
        full_path = os.path.join(folder_path, file)
        with open(full_path, 'r') as f:
            data = json.load(f)
            rank_score = data['ranking_score']
            ranking_score[full_path] = rank_score
    if ranking_score:
        best_file = max(ranking_score, key=ranking_score.get)
        match = re.search(r"summary_confidences_(\d)\.json", best_file)
        if match:
            best_file_num = match.group(1)
            st.write(f"**:sparkles: Best model is:** number {best_file_num} with a ranking score of :blue-background[{ranking_score[best_file]}]")
            selected_model= get_model_number(int(best_file_num))
    else:
        st.write("No matching files found.")
        
    return selected_model
    