import streamlit as st

from lab_helpers_diabetes import load_data
from optimisation import PRIORITY_FEATURES, choose_patient

test = load_data()["test"]

st.write("Tick the candidate patients, then press OK")

rows = st.dataframe(
    test,
    on_select="rerun"
).selection.rows

if st.button("OK") and rows:
    patients = test.iloc[rows]

    x = patients[PRIORITY_FEATURES]

    span = (x.max() - x.min()).replace(0, 1)

    scaled = (
        100 * (x - x.min()) / span
    ).round().astype(int)

    selected_index = choose_patient(
        scaled.values.tolist()
    )

    st.write("Selected patient")

    st.dataframe(
        patients.iloc[[selected_index]]
    )