import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col5, col2= st.columns(3)


with col1:
    st.image("images/Lekan.jpg", width=300 )

with col2:
    st.title("Olalekan Amos Adewopo")
    content = """ Hello, my name is Olalekan Adewopo Amos. I am a dedicated IT leader with over 8 years of experience in Site Reliability Engineering (SRE), DevOps, and Cloud Engineering. I have a proven track record in designing, implementing, and optimizing resilient, scalable systems that drive operational excellence and ensure the high availability of critical applications.

I excel at leveraging industry-leading tools like Kubernetes for container orchestration and Dynatrace for comprehensive monitoring and performance optimization. My approach combines innovative problem-solving, collaborative teamwork, and a passion for continuous improvement.

Additionally, I am aspiring to become a Full Stack Python Developer, aiming to expand my technical expertise and contribute to building robust end-to-end solutions."""
    st.write(content)

with col5:
    st.image("images/aws.jpg", width=100)
    st.image("images/dynatrace.png", width=100)
    st.image("images/k8.png", width=100)

st.text("Below you can find some of the apps i have built in python . Feel free to contact me!")

col3, empty_col,  col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source Code]({row['url']})")