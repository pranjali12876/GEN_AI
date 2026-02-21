import streamlit as st
import pandas as pd
import numpy as np

#Displaying Text Content
st.title("My First STREAMLIT App")
st.write("Hello Meow this side")
st.text("Lets start")

#Creating Charts using Pandas & Numpy
df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

#Sidebar,Image & Video
st.sidebar.title("Navigation")
st.write("Hey Meows here")
st.image("images.jpg")
st.video("https://www.youtube.com/watch?v=XDKUeCmx_hs")

#File Upload(csv)
upload_file=st.file_uploader("Upload a csv file",type='csv')

if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)

#Taking User Input
name=st.text_input("Enter name: ")
if st.button("Welcome"):
    st.success(f"Hello,{name}")
       
#Text & Markdown Formatting
st.header("This is a header ")
st.subheader("This is a subheader ")

st.markdown("**Bold**,*Italic*,'Code',[Link](https://streamlit.io)")
st.code("for i in range(5):print(i)",language="python")

st.text_input("What is Your Name?")
st.text_area("write something...")
st.number_input("Pick a number",min_value=0,max_value=100)
st.slider("Choose a range",0,100)
st.selectbox("Select a fruit",["Apple","Banana","Mango"])
st.multiselect("Choose Toppings",["Cheese","Tomato","Olives"])
st.radio("Pick One",["Option A","Option B"])
st.checkbox("I agree to the terms")

#Matplotlib Integration

import matplotlib.pyplot as plt 
fig,ax=plt.subplots()
ax.plot([1,2,3],[1,4,9])

st.pyplot(fig)