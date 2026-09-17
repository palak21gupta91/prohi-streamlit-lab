import streamlit as st
from lab_helpers_diabetes import load_data

st.dataframe(load_data()["train"])