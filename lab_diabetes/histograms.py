import streamlit as st
from matplotlib.figure import Figure
from lab_helpers_diabetes import load_data, FEATURES

df = load_data()["train"]

feature = st.selectbox("Feature", FEATURES)

fig = Figure()
fig.subplots().hist(df[feature])

st.pyplot(fig)