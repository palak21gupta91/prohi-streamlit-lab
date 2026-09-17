import streamlit as st
from matplotlib.figure import Figure
from lab_helpers_breast_cancer import load_data

df = load_data()["train"]

feature = st.selectbox(
    "Feature",
    ["mean radius", "mean texture", "mean area"]
)

fig = Figure()
fig.subplots().hist(df[feature])

st.pyplot(fig)