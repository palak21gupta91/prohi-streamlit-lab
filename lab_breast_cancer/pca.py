import streamlit as st
import plotly.express as px

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from lab_helpers_breast_cancer import load_data, CLASS_NAMES, FEATURES

df = load_data()["train"]

X = StandardScaler().fit_transform(df[FEATURES])

Z = PCA(n_components=3).fit_transform(X)

st.plotly_chart(
    px.scatter_3d(
        x=Z[:, 0],
        y=Z[:, 1],
        z=Z[:, 2],
        color=df["class"].map(CLASS_NAMES)
    )
)