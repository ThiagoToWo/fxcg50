#Sorteia repetidamen-
#te 15 letras ate
#formar a frase alvo,
#mostrando a quanti-
#dade de letras cor-
#retas
from evolucao import *

dnaf='eu sou o melhor'
ldna=len(dnaf)
dnai=rnddna(ldna)
best=dnai
adap=0

while adap<ldna:
  rand=rnddna(ldna)
  adap=snadap(dnai,dnaf)
  display(rand,adap)