#####################
#Enquanto a frase nao
#se forma, faz cops
#copias da frase atu-
#al verifica qual de-
#las melhor se adapta
#e atuliza a melhor
#frase com ela
from evolucao import *

dnaf='eu sou o melhor'
ldna=len(dnaf)
dnai=rnddna(ldna)
best=dnai
adap=0
cops=100
pmut=0.005

while adap<ldna:
  copies=sncopy(best,cops,pmut)
  snb=snbest(copies,dnaf)
  best=snb[0]
  adap=snb[1]
  display(best,adap)