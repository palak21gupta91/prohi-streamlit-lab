import streamlit as st

page1 = st.Page("tablepage.py", title="tablepage", icon="📋")
page2 = st.Page("histograms.py", title="histograms", icon="📊")
page3 = st.Page("pca.py", title="PCA", icon="🔍")
page4 = st.Page("predictive.py", title="Predictive", icon="🤖")

st.navigation([page1, page2, page3, page4]).run()