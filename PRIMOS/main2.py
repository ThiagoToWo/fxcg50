#Verifica a relacao
# 10**n < p(n+2)#
#Imprime 10**n,
#o primorial p(n+2)#
#e a verificacao da
#desigualdade
from primos import *

n=739
p=seqprim(n)
phash=2
min=1

print("10**n","p(n+2)#","10**n<p(n+2)#")

for i in range(1,len(p)):
  phash*=p[i]
  print("{:.0e}".format(min),"{:.2e}".format(phash),min<phash)
  min*=10