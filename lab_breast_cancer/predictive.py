import streamlit as st

from sklearn.model_selection import cross_validate
from sklearn.tree import DecisionTreeClassifier, plot_tree

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

from lab_helpers_breast_cancer import load_data, FEATURES, CLASS_NAMES
import streamlit as st

from sklearn.model_selection import cross_validate
from sklearn.tree import DecisionTreeClassifier

from lab_helpers_breast_cancer import load_data, FEATURES, CLASS_NAMES

data = load_data()
train = data["train"]
test = data["test"]

X = train[FEATURES]
y = train["class"]

depth = st.slider("Max depth", 1, 10, 4)

model = DecisionTreeClassifier(max_depth=depth)

cv = cross_validate(
    model,
    X,
    y,
    cv=5,
    return_estimator=True
)

accuracy = cv["test_score"].mean()

st.write("Accuracy:", accuracy)

best_model = cv["estimator"][cv["test_score"].argmax()]

first_patient = test[FEATURES].iloc[[0]]

prediction = best_model.predict(first_patient)[0]

st.write("Prediction for first test patient:", CLASS_NAMES[prediction])
st.write("Tick one patient, then press OK")

test = load_data()["test"]

rows = st.dataframe(
    test,
    on_select="rerun",
    selection_mode="single-row"
).selection.rows

if st.button("OK") and rows:
    selected_patient = test.iloc[[rows[0]]]

    prediction = best_model.predict(selected_patient[FEATURES])[0]

    st.write(
        "The prediction is:",
        CLASS_NAMES[prediction]
    )
    from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from sklearn.tree import plot_tree

st.write("Decision tree")

fig = Figure(figsize=(12, 6), layout="constrained")
FigureCanvasAgg(fig)

ax = fig.subplots()

plot_tree(
    best_model,
    ax=ax,
    feature_names=FEATURES,
    class_names=["B", "M"],
    filled=True,
    label="none",
    fontsize=14
)

for text in ax.texts:
    lines = text.get_text().split("\n")
    text.set_text(
        lines[0].replace(" <= ", "\n <=\n")
        if " <=" in lines[0]
        else lines[-1]
    )

st.pyplot(fig)
import pandas as pd

st.write("Feature importance")

importance = pd.Series(
    best_model.feature_importances_,
    index=FEATURES
)

st.bar_chart(
    importance[importance > 0].sort_values()
)