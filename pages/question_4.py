import streamlit as st
from PIL import Image
st.title("4/ Compléter les lignes 4, 5 et 8 du programmes ci dessous")
image = Image.open('enonce.jpg')
st.image(image, caption = 'énoncé du cours')


code = '''def nombres_solutions(a,b,c):
    discrimnant = delta(a, b, c)
    if discriminant < 0:
        return 0
    elif discriminant ==0:
        return 1
    else:
        return 2'''
st.code(code, language = 'python')
    
