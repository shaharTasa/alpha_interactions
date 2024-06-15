import numpy as np

def extract_data_from_json(json_data, json_details):
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


# def extract_data_from_json(json_data, json_details):
#     # Check that json_details is not empty and is a list
#     if not json_details or not isinstance(json_details, list):
#         raise ValueError("json_details must be a non-empty list")
    
#     # Extract the first item (assuming there's at least one item based on the check above)
#     first_detail = json_details[0]
    
#     # Check that the necessary keys exist in the first item
#     if 'sequences' not in first_detail or 'name' not in json_data:
#         raise KeyError("Missing 'sequences' in json_details or 'name' in json_data")
    
#     sequences = [seq['proteinChain']['sequence'] for seq in first_detail['sequences']]
#     sequences_len = [len(seq) for seq in sequences]
#     proteins_names = json_data['name']
    
#     # Ensure all required keys exist in json_data
#     required_keys = ['pae', 'atom_plddts', 'contact_probs', 'token_chain_ids', 'atom_chain_ids']
#     if not all(key in json_data for key in required_keys):
#         missing_keys = [key for key in required_keys if key not in json_data]
#         raise KeyError(f"Missing keys in json_data: {', '.join(missing_keys)}")
    
#     full_pae = np.array(json_data['pae'])
#     atom_plddts = np.array(json_data['atom_plddts'])
#     contact_probs = np.array(json_data['contact_probs'])
#     token_chain_ids = np.array(json_data['token_chain_ids'])
#     atom_chain_ids = np.array(json_data['atom_chain_ids'])
#     unique_chain_ids = np.unique(token_chain_ids)

#     return sequences_len, sequences, proteins_names, full_pae, atom_plddts, contact_probs, token_chain_ids

# def extract_data_from_json(full_data_json, job_request_json):
#     try:
#         sequences_len = [len(seq['proteinChain']['sequence']) for seq in job_request_json[0]['sequences']]
#         sequences = [seq['proteinChain']['sequence'] for seq in job_request_json[0]['sequences']]
#         proteins_names = job_request_json[0]['name']
#         full_pae = np.array(full_data_json['pae'])
#         atom_plddts = np.array(full_data_json['atom_plddts'])
#         contact_probs = np.array(full_data_json['contact_probs'])
#         token_chain_ids = np.array(full_data_json['token_chain_ids'])
#         atom_chain_ids = np.array(full_data_json['atom_chain_ids'])  # Assume this was missing
        
#         # Placeholder for interactions calculation if not done here
#         interactions = []  # You need to replace this with actual interaction calculation logic if needed

#         return sequences_len, sequences, proteins_names, full_pae, atom_plddts, contact_probs, token_chain_ids, interactions
#     except KeyError as e:
#         # Handle missing keys in JSON structure
#         raise ValueError(f"Key error in JSON data: {e}")