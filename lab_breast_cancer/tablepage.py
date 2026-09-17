import streamlit as st
from lab_helpers_breast_cancer import load_data

st.dataframe(load_data()["train"])