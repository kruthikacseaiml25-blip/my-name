import streamlit as st

# Title
st.title("My First Streamlit App")

# User input
name = st.text_input("Enter your name")

# Button
if st.button("Submit"):
    st.success(f"Welcome, {name}!")