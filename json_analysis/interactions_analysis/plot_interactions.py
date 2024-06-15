from streamlit_molstar import st_molstar
import plotly.express as px
import glob
import os
from streamlit_molstar.auto import st_molstar_auto
from stmol import showmol
import py3Dmol
from stmol import *

def create_scatter_plot(df_interactions):
    # Label for interaction pairs
    df_interactions['Interaction'] = df_interactions['Chain_1'] + ' :' + df_interactions['Residue_1'] + ' - ' + df_interactions['Position_1'].astype(str) \
                                    + ' <--> ' + df_interactions['Chain_2'] + ' :' + df_interactions['Residue_2'] + ' - ' + df_interactions['Position_2'].astype(str)

    # Create the scatter plot
    fig = px.scatter(df_interactions, x='Probability', y='PAE', color='Interaction',
                     hover_data=['Interaction'], title="Interaction Scatter Plot",
                     labels={'PAE': 'Predicted Aligned Error', 'Probability': 'Contact Probability'})
    
    # Update layout if necessary
    fig.update_layout(
        xaxis_title="Contact Probability",
        yaxis_title="Predicted Aligned Error",
        legend_title="Interaction Pairs"
    )
    
    return fig


def visualization_protein(folder_path,model_number):

    pattern = f"*_model_{model_number}.cif"
    found_files = glob.glob(os.path.join(folder_path, pattern))
    print(found_files)
    if found_files:
        cif_file_path = found_files[0]
        st_molstar(cif_file_path, key='3')

