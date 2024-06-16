import numpy as np

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

def extract_data_from_summary(json_data):
    
