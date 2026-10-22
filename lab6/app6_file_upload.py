import streamlit as st
import pandas as pd

st.title("Lab 6: File Upload and Pandas DataFrames")

st.write("Upload a CSV file to view and analyze its data.")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    st.subheader("Data Summary")
    st.write("Number of rows:", df.shape[0])
    st.write("Number of columns:", df.shape[1])

    st.subheader("Column Names")
    st.write(list(df.columns))

    st.subheader("Statistical Summary")
    st.write(df.describe())

    st.subheader("Missing Values")
    st.write(df.isnull().sum())
else:
    st.info("Please upload a CSV file to begin.")