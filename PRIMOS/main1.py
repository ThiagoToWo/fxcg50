#Imprime a posicao n,
#o n-esimo primo e o
#primeiro numero com
#n fatores primos 
#distintos
from primos import *

n=1100
p=seqprim(n)
phash=1

print("n","p(n)","p(n)#")

for i in range(len(p)):
  phash*=p[i]
  print(i+1,p[i],phash)