import streamlit as st

st.title("Lab 3: Streamlit Layouts")

st.header("Columns")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Column 1")
    st.write("This is the first column.")

with col2:
    st.subheader("Column 2")
    st.write("This is the second column.")

st.divider()

st.header("Sidebar")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a page",
    ["Home", "About"]
)

if page == "Home":
    st.write("Welcome to the Home page!")
else:
    st.write("This is the About page.")

st.divider()

st.header("Tabs")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("This is the first tab.")

with tab2:
    st.write("This is the second tab.")

st.divider()

st.header("Container")

with st.container():
    st.write("These elements are inside a container.")
    st.success("Layout demonstration completed!")