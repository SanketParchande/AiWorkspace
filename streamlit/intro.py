import streamlit as st

st.title("Introduction to Streamlit")
st.write("Sample application test using streamlit for square of number.")

#Create a slider to select a number
st.header("Square Calculator")
number = st.slider("Pick a number", 0, 100, 25)#min, max, default
square = number ** 2
st.subheader('Result')
st.write(f"The square of {number} is {square}.")