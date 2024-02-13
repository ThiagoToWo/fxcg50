#Imprime a quantidade
#de passos do metodo
#tradicional (td) e
#do metodo de divisao
#sucessiva (sd) para
#achar os divisores
#de n no intervalo
#[init,init+200]
from divisors import *

init=1
for i in range(init,init+200):
  td=traddiv(i)
  sd=succdiv(i)
  print("n:",i,"td:",td[1],"sd:",sd[1])