
import streamlit as st

def get_model_number(best_num):
    
    st.markdown("you can change here to a different model:",help="The model samples five predictions per seed. The top ranked prediction is displayed on the result page.")
    model_num = range(0,5)
    selected_model = st.selectbox('', model_num , label_visibility='collapsed',index=best_num)
    return selected_model
