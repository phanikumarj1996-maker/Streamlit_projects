import streamlit as st
import pandas as pd

st.title("Lab 5: Data Visualization")
st.header("Student Marks Analysis")

data = {
    "Student": ["Ravi", "Priya", "Kiran", "Anu", "Rahul"],
    "Maths": [85, 90, 78, 92, 88],
    "Science": [80, 95, 82, 89, 84]
}

df = pd.DataFrame(data)

st.subheader("Student Marks")
st.dataframe(df)

st.subheader("Bar Chart")
st.bar_chart(df.set_index("Student"))

st.subheader("Line Chart")
st.line_chart(df.set_index("Student"))

st.subheader("Summary")
st.write("Average Maths Marks:", df["Maths"].mean())
st.write("Average Science Marks:", df["Science"].mean())