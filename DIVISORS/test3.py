#Compara os dois
#metodos de achar
#divisores com
#contagem de passos
from divisors import *

n=461

td=traddiv(n)
nd=succdiv(n)

print("Metodo Tradicional")
print("Passos:",td[1])
print("#Divisores:",len(td[0]))
print(td[0])

print("Divisao Sucessiva")
print("Passos:",nd[1])
print("#Divisores:",len(nd[0]))
print(nd[0])