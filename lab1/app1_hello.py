import streamlit as st

st.set_page_config(
    page_title="Hello App",
    page_icon="👋",
    layout="centered"
)

st.title("Hello Streamlit")
st.header("My First App")
st.subheader("Learning Basics")

st.write("Streamlit converts Python scripts into web apps.")

st.markdown("**Bold text**, *italic text*, and `code`.")

st.success("App loaded successfully!")
st.info("This is an info message.")
st.warning("This is a warning.")
st.error("This is an error.")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=100)

st.write("### Sample Data")
st.table({"Name": ["A", "B"], "Marks": [85, 90]})

if name:
    st.write("Your name is:", name)
    st.write("Your age is:", age)