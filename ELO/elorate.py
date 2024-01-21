from random import *
from math import *

a=int(input("Seu ELO: "))
k=32

b=int(input("ELO adversario\n(sair=0): "))

while b!=0:
  pa=1/(1+10**((b-a)/400))
  pb=1-pa
  print("Prob. vitoria:","{:.2%}".format(pa))
  result=int(input("Escolha o resultado:\n"+
  "\tVenceu (1)\n"+
  "\tEmpatou (2)\n"+
  "\tPerdeu (3)\n"+
  "Resultado: "))

  if result==1:
    sa=1
    sb=0
  elif result==2:
    sa=0.5
    sb=0.5
  elif result==3:
    sa=0
    sb=1
  else:
    print("Valor invalido")
    break
  
  tempa=a
  tempb=b
  a+=k*(sa-pa)
  b+=k*(sb-pb)
  
  print("Seu novo ELO:\n",round(tempa),"->",round(a))
  print("Novo ELO adver.:\n",round(tempb),"->",round(b))
  b=int(input("Prox. adversario\n(sair=0): "))