import streamlit as st

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/Lekan.jpg", width=300)

with col2:
    st.title("Olalekan Amos Adewopo")
    content = """ HI my name is Olalekan , I'm an Aspiring Python programmer but a professional in Containers and SRE"""
    st.write(content)