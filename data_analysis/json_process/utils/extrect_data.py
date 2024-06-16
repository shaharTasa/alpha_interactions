import numpy as np
import os
import json
import streamlit as st
import pandas as pd
import plotly.express as px
from draws.check_method import checkbox_method

def extract_data_from_full_data_json(json_data, json_details):
    sequences_len = [len(seq['proteinChain']['sequence']) for seq in json_details[0]['sequences']]
    sequences = [seq['proteinChain']['sequence'] for seq in json_details[0]['sequences']]
    proteins_names = json_details[0]['name']
    full_pae = np.array(json_data['pae'])
    atom_plddts = np.array(json_data['atom_plddts'])
    contact_probs = np.array(json_data['contact_probs'])
    token_chain_ids = np.array(json_data['token_chain_ids'])
    atom_chain_ids = np.array(json_data['atom_chain_ids'])
    unique_chain_ids = np.unique(token_chain_ids)
    return sequences_len,sequences,proteins_names,full_pae,atom_plddts,contact_probs,token_chain_ids

def extract_data_from_summary(json_data,folder_path):
    
    full_path = os.path.join(folder_path, json_data)
    with open(full_path, 'r') as f:
        data = json.load(f)
        chain_iptm = data['chain_iptm']
        chain_pair_iptm = data['chain_pair_iptm']
        chain_pair_pae_min = data['chain_pair_pae_min']
        iptm = data['iptm']
        ptm = data['ptm']
        ranking_score = data['ranking_score']
        # chain_ptm = data['chain_ptm']
        # fraction_disordered = data['fraction_disordered']
        # has_clash = data['has_clash']
        # num_recycles = data['num_recycles']

    checkbox_method(f"**ptm** : {str(ptm)}","A scalar in the range 0-1 indicating the predicted TM-score for the full structure.")
    checkbox_method(f'**iptm** :{iptm}','A scalar in the range 0-1 indicating predicted interface TM-score (confidence in the predicted interfaces) for all interfaces in the structure.')
    checkbox_method(f"**chain iptm** : {str(chain_iptm).replace('[', '').replace(']','')}",'chain_iptm is The average confidence (interface pTM) in the interface between each chain and all other chains.')
    checkbox_method(f"**chain pair iptm**: {str(chain_pair_iptm[0]).replace('[', '').replace(']',''),str(chain_pair_iptm[1]).replace('[', '').replace(']','')}",f'A (num_chains, num_chains) array. Off-diagonal element (i, j) of the array contains the ipTM restricted to tokens from chains i and j. Diagonal element (i, i) contains the pTM restricted to chain i. Can be used for ranking a specific interface between two chains, when you know that they interact.')
    checkbox_method(f"**chain pair pae min** : {str(chain_pair_pae_min[0]).replace('[', '').replace(']',''),str(chain_pair_pae_min[1]).replace('[', '').replace(']','')}",' A (num_chains, num_chains) array. Element (i, j) of the array contains the lowest PAE value across rows restricted to chain i and columns restricted to chain j. This has been found to correlate with whether two chains interact or not, and in some cases can be used to distinguish binders from non-binders.')
    checkbox_method(f"**ranking_score** : {str(ranking_score)}",'A scalar in the range [-100, 1.5] that can be used for ranking predictions.')
    

