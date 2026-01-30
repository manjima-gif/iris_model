import streamlit as st
import pandas as pd 
import pickle 
import numpy as num 
import os 
st.set_page_config(page_title="iris classifier",page_icon="❤️")
@st.cache_resource
def load_model():
  model_path="iris_model.pkl"
  if os.path.exists(model_path):
    with open(model_path,'rb')as file:
      return pickle.load(file)
  else:
    st.error(f"Model file'{modal_path}'not found !")
    return None

model = load_model()
