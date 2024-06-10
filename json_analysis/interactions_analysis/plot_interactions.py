import matplotlib.pyplot as plt

# Assuming inter_chain_interactions is structured as follows:
# [(chain_id1, residue1, position1, chain_id2, residue2, position2, PAE, contact_prob), ...]

# Extracting data for plotting
pae_values = [interaction[6] for interaction in inter_chain_interactions]
contact_probs = [interaction[7] for interaction in inter_chain_interactions]
chain_pairs = [f"{interaction[0]}-{interaction[4]}" for interaction in inter_chain_interactions]

# Create a scatter plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(pae_values, contact_probs, c=pae_values, cmap='viridis', alpha=0.6, edgecolors='w', linewidths=0.5)

# Adding color bar
plt.colorbar(scatter, label='Predicted Aligned Error (PAE)')

# Adding titles and labels
plt.title('Inter-Chain Interactions: PAE vs Contact Probabilities')
plt.xlabel('Predicted Aligned Error (PAE)')
plt.ylabel('Contact Probability')
plt.grid(True)

# Optionally, annotate some points
for i, chain_pair in enumerate(chain_pairs):
    if i % 5 == 0:  # Annotate every 5th point for clarity
        plt.annotate(chain_pair, (pae_values[i], contact_probs[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()
