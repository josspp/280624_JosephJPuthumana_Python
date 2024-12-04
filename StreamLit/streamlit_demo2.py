import streamlit as st

st.title("User input Demo")



username = st.text_input("Username:")
st.write("Input username is", username)

password= st.text_input("Password:")
st.write("input password is", password)

