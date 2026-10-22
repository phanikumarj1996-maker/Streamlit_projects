import streamlit as st
import json

st.title("Lab 10: API Integration + JSON + Secrets")

st.subheader("JSON Playground")

data = {
    "name": st.text_input("Enter your name", "Student"),
    "course": st.selectbox("Select course", ["B.Tech", "BCA", "MCA"]),
    "year": st.number_input("Year of study", 1, 4, 2)
}

if st.button("Generate JSON"):
    json_data = json.dumps(data, indent=4)
    st.code(json_data, language="json")

st.subheader("API Integration")

if st.button("Fetch API Data"):
    import requests

    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/1",
            timeout=10
        )
        response.raise_for_status()
        st.json(response.json())
    except requests.RequestException as e:
        st.error(f"API request failed: {e}")