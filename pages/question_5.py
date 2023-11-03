import streamlit as st
from math import*
import matplotlib.pyplot as plt
import numpy as np

def delta (n1,n2,n3):
        D=n2**2-4*n1*n3
        return D

def resolution(n1,n2,n3):    
    if n1==0:
        return "ce n'est pas une equation du 2nd degré"
    else:
        x=delta(n1,n2,n3)
        if x == 0:
            return "une racine double" , round(((-n2)/(2*n1)),2)
        elif x<0:
            return "le dicriminant est négatif donc il n'y a pas de solutions"
        else:
          
            return "le discrimant est positif donc il y a deux solutions: ",round(((-n2-sqrt(x))/(2*n1)),2),round(((-n2+sqrt(x))/(2*n1)),2)

st.title("5/ Ecrire un autre programme qui donne les solutions losrqu'elles existent")
code = '''from math import*
a = int(input("quelle est la valeur de a?"))
b = int(input("quelle est la valeur de b?"))
c = int(input("quelle est la valeur de c?"))
def delta (n1,n2,n3):
    D=n2**2-4*n1*n3
    return D

if a==0:
    print("cette équation n'est pas du second degré")
else:
    x=delta(a,b,c)
    if x == 0:
        print("le discriminant est nul donc il y a une solution:",(-b)/(2*a))
    elif x<0:
        print("le dicriminant est négatif donc il n'y a pas de solutions")
    else:
        print("le discrimant est positif donc il y a deux solutions: ",(-b-sqrt(x))/(2*a)," et",(-b+sqrt(x))/(2*a))'''
st.code(code, language = 'python')
st.text("Déterminer les facteurs du polynome a*x²+b*x+c")
a = st.slider('a=', -100, 100, 1)
b = st.slider('b=', -100, 100, 1)
c = st.slider('c=', -100, 100, 1)
st.write ( a,"x²  +",b,"x +",c ," =  0")
D=delta (a,b,c)
st.write ("discriminant = ",D)
resultat = resolution(a,b,c)
st.write(resultat)

x = np.linspace(-10, 10, 70)
y1 = a*(x)** 2+b*(x)+c
y2=0*x
fig, ax = plt.subplots()
ax.plot(x,y1)
ax.plot(x,y2)
plt.title('Polynome du second degré')
plt.axis((-10, 10, -2, 10))

#-------Affichage de la grille------------
grid_x_ticks = np.arange(-2,2, 1)
grid_y_ticks = np.arange(-2, 10, 1)
ax.set_xticks(grid_x_ticks , minor=True)
ax.set_yticks(grid_y_ticks , minor=True)
ax.grid(which='both')

st.pyplot(fig)
