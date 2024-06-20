from streamlit_molstar import st_molstar
import plotly.express as px


def create_scatter_plot(df_interactions):
    df_interactions['Interaction'] = df_interactions['Chain_1'] + ' :' + df_interactions['Residue_1'] + ' - ' + df_interactions['Position_1'].astype(str) \
                                    + ' <--> ' + df_interactions['Chain_2'] + ' :' + df_interactions['Residue_2'] + ' - ' + df_interactions['Position_2'].astype(str)

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


def visualization_protein(found_files):
    cif_file_path = found_files[0]
    st_molstar(cif_file_path, key='3',height=400)



    