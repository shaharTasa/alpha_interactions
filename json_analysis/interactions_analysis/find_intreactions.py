import json
import numpy as np


def read_json_file(file_path):
    with open(file_path) as f:
        json_data = json.load(f)
    return json_data

json_data = read_json_file('C:\\Users\\shach\\Documents\\Alpha_interactions\\json_analysis\\json_output\\fold_Irrc75b_femnb1\\fold_lrrc75b_femnb1_full_data_0.json')
json_details = read_json_file('C:\\Users\\shach\\Documents\\Alpha_interactions\\json_analysis\\json_output\\fold_Irrc75b_femnb1\\fold_lrrc75b_femnb1_job_request.json')


sequences_len = [len(seq['proteinChain']['sequence']) for seq in json_details[0]['sequences']]
sequences = [seq['proteinChain']['sequence'] for seq in json_details[0]['sequences']]
proteins_names = json_details[0]['name']


full_pae = np.array(json_data['pae'])
atom_plddts = np.array(json_data['atom_plddts'])
contact_probs = np.array(json_data['contact_probs'])
token_chain_ids = np.array(json_data['token_chain_ids'])
atom_chain_ids = np.array(json_data['atom_chain_ids'])
unique_chain_ids = np.unique(token_chain_ids)

pae_threshold = 5
contact_prob_threshold = 0.1

num_tokens = full_pae.shape[0]
unique_chain_ids = np.unique(token_chain_ids)
chains = {chain_id: index+1 for index, chain_id in enumerate(unique_chain_ids)}
inter_chain_interactions = []
unique_chain_ids
for idx1 in range(len(unique_chain_ids)):
    for idx2 in range(idx1 + 1, len(unique_chain_ids)):
        chain_id1 = unique_chain_ids[idx1]
        chain_id2 = unique_chain_ids[idx2]
        indices_chain1 = [i for i, x in enumerate(token_chain_ids) if x == chain_id1]
        indices_chain2 = [j for j, x in enumerate(token_chain_ids) if x == chain_id2]
        print(indices_chain2)

        for i in indices_chain1:
            for j in indices_chain2:
                if full_pae[i, j] <= pae_threshold and contact_probs[i, j] >= contact_prob_threshold:

                    pos_i = i - indices_chain1[0] + 1
                    pos_j = j - indices_chain2[0] + 1
                    interaction = (chain_id1, sequences[idx1][pos_i - 1], pos_i, 
                                   sequences[idx2][pos_j - 1], pos_j, chain_id2, 
                                   full_pae[i, j], contact_probs[i, j])
                    inter_chain_interactions.append(interaction)

print(f'input name: {proteins_names}')
for i, seq_len in enumerate(sequences_len):
    print(f"Length of sequence {chr(65+i)}: {seq_len}")
average_plddt = atom_plddts.sum() / len(atom_plddts)
print(f'Average pLDDT: {average_plddt:.2f}')

print("High-confidence inter-chain interactions (Chain 1, Residue, Position, Chain 2, Residue, Position, PAE, Contact Probability):")
for interaction in inter_chain_interactions:
    print(interaction)

