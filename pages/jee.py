import streamlit as st
import pandas as pd


st.title("Jee")

df=pd.read_csv("C:/Users/Harshan/Desktop/mysite/Total Seats.csv")
st.write(df)

st.bar_chart(df, x="Branch of Study", y="Total Seats" )
dg=pd.read_csv("C:/Users/Harshan/Desktop/mysite/All IIT List of Percentile.csv")
st.write(dg)
st.bar_chart(dg,x="IIT/Branch", y=["General","SC","ST","OBC"] )

