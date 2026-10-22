import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.title("Lab 8: Iris Flower Prediction")
st.write("Predict the Iris flower species using machine learning.")

# Load dataset and train the model
iris = load_iris()
X = iris.data
y = iris.target

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

st.subheader("Enter Flower Measurements")

sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

if st.button("Predict Flower"):
    features = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    prediction = model.predict(features)[0]
    species = iris.target_names[prediction]

    st.success(f"Predicted Iris species: {species}")

    probabilities = model.predict_proba(features)[0]
    probability_df = pd.DataFrame({
        "Species": iris.target_names,
        "Probability": probabilities
    })

    st.subheader("Prediction Probabilities")
    st.bar_chart(probability_df.set_index("Species"))