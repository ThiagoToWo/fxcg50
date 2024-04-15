#Conjunto de funcoes
#para simular o jogo
#dice poker
from random import random
from math import floor

#Conta a frequencia
#de cada valor i no
#dado d e acumula na
#lista f em f[i] 
def freq(d,f):
  for i in range(5):
    if d[i]==1:
      f[1]+=1
    elif d[i]==2:
      f[2]+=1
    elif d[i]==3:
      f[3]+=1
    elif d[i]==4:
      f[4]+=1
    elif d[i]==5:
      f[5]+=1
    else:
      f[6]+=1

#Joga os 5 dados e
#conta a frequencia
#de cada valor
def play(d,f):
  for i in range(5):
    d[i]=1+floor(random()*6)
  freq(d,f)  

#Verifica se ocorreu
#um five, dada a lis-
#ta de frequencias f
def isfive(f):
  tem5=False
  for i in range(1,7):
    if f[i]==5:
      tem5=True
  return tem5

#Verifica se ocorreu
#um four, dada a lis-
#ta de frequencias f
def isfour(f):
  tem4=False
  for i in range(1,7):
    if f[i]==4:
      tem4=True
  return tem4

#Verifica se ocorreu
#um straight, dada a lis-
#ta de frequencias f
def isstraight(f):
  ls=True
  ts=True
  for i in range(1,6):
    if f[i]!=1:
      ls=False 
  for i in range(2,7):
    if f[i]!=1:
      ts=False 
  return ls or ts

#Verifica se ocorreu
#um full house, dada a lis-
#ta de frequencias f
def isfullhouse(f):
  tem2=False
  tem3=False
  for i in range(1,7):
    if f[i]==2:
      tem2=True
    elif f[i]==3:
      tem3=True
  return tem2 and tem3

#Verifica se ocorreu
#um three, dada a lis-
#ta de frequencias f
def isthree(f):
  tem2=False
  tem3=False
  for i in range(1,7):
    if f[i]==2 or f[i]>3:
      return False
    elif f[i]==3:
      tem3=True
  return tem3

#Verifica se ocorreu
#um 2 pair, dada a lis-
#ta de frequencias f  
def is2pair(f):
  p=0
  for i in range(1,7):
    if f[i]==2:
      p+=1
  if p==2:
    return True
  else:
    return False

#Verifica se ocorreu
#um pair, dada a lis-
#ta de frequencias f
def ispair(f):
  p=0
  for i in range(1,7):
    if f[i]==2:
      p+=1
    elif f[i]>1:
      return False
  if p==1:
    return True
  else:
    return False