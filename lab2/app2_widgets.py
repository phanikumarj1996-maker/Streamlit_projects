import streamlit as st

st.title("Lab 2: Widgets Playground")

st.header("User Information")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=100)
city = st.selectbox(
    "Select your city",
    ["Ongole", "Chennai", "Hyderabad", "Other"]
)

rating = st.slider("Rate this app", 1, 10, 5)

if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("City:", city)
    st.write("Rating:", rating)