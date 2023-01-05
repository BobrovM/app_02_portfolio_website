import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Fake Company")

content = "Fake text. Fake text. Fake text. Fake text." \
          "Fake text. Fake text. Fake text. Fake text."
st.write(content)

st.header("Our Team")

col1, empty_col_1, col2, empty_col_2, col3 = st.columns([2, 0.5, 2, 0.5, 2])

df = pandas.read_csv("student_projects/day_22/data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.header(str(row["first name"]).capitalize()+" "+
                  str(row["last name"]).capitalize())
        st.write(row["role"])
        st.image("student_projects/day_22/images/"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(str(row["first name"]).capitalize()+" "+
                  str(row["last name"]).capitalize())
        st.write(row["role"])
        st.image("student_projects/day_22/images/"+row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.header(str(row["first name"]).capitalize()+" "+
                  str(row["last name"]).capitalize())
        st.write(row["role"])
        st.image("student_projects/day_22/images/"+row["image"])
