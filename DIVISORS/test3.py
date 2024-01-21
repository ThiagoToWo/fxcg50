#Compara os dois
#metodos de achar
#divisores com
#contagem de passos
from divisors import *

n=108

print("Metodo Tradicional")
print("Passos",end=": ")
td=traddiv(n)
print("Divisores:",len(td))
print(td)

print("Metodo Novo")
print("Passos",end=": ")
nd=newdiv(n)
print("Divisores:",len(nd))
print(nd)