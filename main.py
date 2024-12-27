import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)


with col1:
    st.image("images/Lekan.jpg", width=300 )

with col2:
    st.title("Olalekan Amos Adewopo")
    content = """ Hello, my name is Olalekan Adewopo Amos. I am a dedicated IT leader with over 8 years of experience in Site Reliability Engineering (SRE), DevOps, and Cloud Engineering. I have a proven track record in designing, implementing, and optimizing resilient, scalable systems that drive operational excellence and ensure the high availability of critical applications.

I excel at leveraging industry-leading tools like Kubernetes for container orchestration and Dynatrace for comprehensive monitoring and performance optimization. My approach combines innovative problem-solving, collaborative teamwork, and a passion for continuous improvement.

Additionally, I am aspiring to become a Full Stack Python Developer, aiming to expand my technical expertise and contribute to building robust end-to-end solutions."""
    st.write(content)

st.text("Below you can find some of the apps i have built in python . Feel free to contact me!")

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])