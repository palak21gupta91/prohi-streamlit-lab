import streamlit as st

page1 = st.Page("tablepage.py", title="tablepage", icon="📋")
page2 = st.Page("histograms.py", title="histograms", icon="📊")
page3 = st.Page("prescriptive.py", title="Prescriptive", icon="🎯")

st.navigation([page1, page2, page3]).run()