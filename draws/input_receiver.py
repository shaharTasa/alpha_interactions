import streamlit as st
import zipfile
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
DATA_STORAGE_PATH = './assets/data_storage'

def draw_file_upload():
    container = st.container(border=True)

    container.write("Upload the ZIP file that contains the output from the AlphaFold server: https://alphafoldserver.com")
    uploaded_file = container.file_uploader("Upload the ZIP file containing all the files", type=['zip'])

    if uploaded_file is not None:
        with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
            folder_name = os.path.splitext(uploaded_file.name)[0]
            new_folder_path = os.path.join(DATA_STORAGE_PATH, folder_name)
            os.makedirs(new_folder_path, exist_ok=True)
            
            zip_ref.extractall(new_folder_path)

        container.success(f"Files uploaded and saved successfully in folder {folder_name}")
        return new_folder_path
    else:
        container.error("Please upload a zip file.")
        
    return None



def draw_input_receiver():
    
    st.write('Choose protein file:')
    col1,col2=st.columns([87,13])
    if os.path.exists(DATA_STORAGE_PATH) and os.path.isdir(DATA_STORAGE_PATH):
        directories = [d for d in os.listdir(DATA_STORAGE_PATH) if os.path.isdir(os.path.join(DATA_STORAGE_PATH, d))]
        # if len(directories) is not 0:
        path_folder = col1.selectbox('', directories,label_visibility='collapsed')
        path = os.path.join(DATA_STORAGE_PATH, path_folder)

    if 'show_upload_file_component' not in st.session_state:
        st.session_state.show_upload_file_component = False
        
    def flip_click_state():
        st.session_state.show_upload_file_component = not st.session_state.show_upload_file_component

    col2.button('Upload', on_click=flip_click_state)

    if st.session_state.show_upload_file_component:
        draw_file_upload()
    
    st.divider()
    return path
