import streamlit as st

st.title("Calculator Demo")


option = st.selectbox(
    "Select your numercal operation",
    ("Add","Subtract","Mutiply","Divide"),
)

st.write("You selected :",option)

numa= st.text_input("NumberA:")
st.write("Input username is",numa)

numb= st.text_input("NumberB:")
st.write("Input username is",numb)

if(option=="Add"):
    result = int(numa)+ int(numb)
    st.text(result)

if(option=="Subtract"):
    result = int(numa) - int(numb)
    st.text(result)

if(option=="Multiply"):
    result = int(numa) * int(numb)
    st.text(result)

if(option=="Divide"):
    result = int(numa) / int(numb)
    st.text(result)


