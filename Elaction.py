import streamlit as st 
import pandas as pd
import numpy as np
st.title("Asslam-o-Alikum")
Name = st.text_input("Enter your Name : ")
Email = st.text_input("Email")
Password = st.text_input("Password")
adr = st.text_area("Enter you addres : ")
button = st.button("Done")

if button :
    st.markdown(f"""
    Name : {Name}
    Email : {Email}
    Password : {Password}
    Addrea : {adr}
""")
st.title("Hello Every Body how are you?")
st.header("We are watch reslts of 2024 Elaction in pakistan.")
st.subheader("We are watch reslt of PB1")
st.image("PB1.png")
st.subheader("We are watch reslt of PB2")
st.image("PB2.png")
st.subheader("We are watch reslt of PB3")
st.image("PB3.png")