import streamlit as st
from PIL import Image
image = Image.open('langage naturel.jpg')
image1 = Image.open('organigramme.jpg')
st.title("1/ Algorithme en langage naturel")
st.image(image, caption = 'langage naturel')
st.image(image1)
