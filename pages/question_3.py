import streamlit as st
d = '''elif'''
st.title("3/ En python, à quoi sert l'instruction elif?")
st.header("L'instruction 'elif' est une combinaison de 'else' et de 'if', elle sert à tester plusieurs conditions succesivement.")
st.subheader("Exemple : On cherche à savoir quels sont les nombres premiers compris entre 1 et 10")
code = '''a=int(input("Valeur de a"))
    if a==5 :
        print("a est un nombre premier nombres entre 1 et 10")
    elif a==1 :
        print("a est un nombre premier nombres entre 1 et 10")
    elif a==2 or 3 or 7 :
        print("a est un nombre premier nombres entre 1 et 10")
    else :
        print("a n'est pas un nombre premier compris entre 1 et 10")'''
st.code(code, language = 'python')
