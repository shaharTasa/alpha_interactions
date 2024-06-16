import json
import numpy as np


def calculate_interactions(sequences, full_pae, contact_probs, token_chain_ids,pae_threshold ,contact_prob_threshold ):
 
    # num_tokens = full_pae.shape[0]
    unique_chain_ids = np.unique(token_chain_ids)
    # chains = {chain_id: index+1 for index, chain_id in enumerate(unique_chain_ids)}
    inter_chain_interactions = []

    for idx1 in range(len(unique_chain_ids)):
        for idx2 in range(idx1 + 1, len(unique_chain_ids)):
            chain_id1 = unique_chain_ids[idx1]
            chain_id2 = unique_chain_ids[idx2]
            indices_chain1 = [i for i, x in enumerate(token_chain_ids) if x == chain_id1]
            indices_chain2 = [j for j, x in enumerate(token_chain_ids) if x == chain_id2]
            for i in indices_chain1:
                for j in indices_chain2:
                    if full_pae[i, j] <= pae_threshold and contact_probs[i, j] >= contact_prob_threshold:
                        pos_i = i - indices_chain1[0] + 1
                        pos_j = j - indices_chain2[0] + 1
                        interaction = (chain_id1, sequences[idx1][pos_i - 1], pos_i,chain_id2,
                                   sequences[idx2][pos_j - 1], pos_j, 
                                   full_pae[i, j], contact_probs[i, j])
                        inter_chain_interactions.append(interaction)
    return inter_chain_interactions

