import random

def shuffle_amino_acids(sequence):
    # Convert the sequence into a list of amino acids
    amino_acids = list(sequence)
    
    # Shuffle the list of amino acids
    random.shuffle(amino_acids)
    
    # Convert the list back to a string
    shuffled_sequence = ''.join(amino_acids)
    
    return shuffled_sequence

# Example usage
sequence = "PYQYPALTPEQKKELSDIAHRIV"
shuffled_sequence = shuffle_amino_acids(sequence)
print("Original sequence:", sequence)
print("Shuffled sequence:", shuffled_sequence)
