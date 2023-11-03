import streamlit as st
st.title("2/ Ecrire en Python une fonction delta(a,b,c) qui retourne le discriminant (E)")
st.header("Ce programme permet de calculer le discriminant d'une fonction du second degré")
def delta (a,b,c):
    Discriminant=b**2-4*a*c
    return Discriminant
code = '''def delta (a,b,c):
    Discriminant=b**2-4*a*c
    return Discriminant'''
st.code(code, language='python')
with st.sidebar:
    st.text("Déterminer les facteurs du polynome a*x²+b*x+c")
    a = st.number_input('a = ', value = 1, step = 1)
    b = st.number_input('b = ', step = 1)
    c = st.number_input('c = ', step = 1)
st.write("discriminant =", delta(a,b,c))
