from math import *
from random import random
from casioplot import *

char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

#Cria uma sequencia
#aleatoria de l
#letras
def rnddna(l):
  dna=''
  for i in range(l):   
    rnd=floor(random()*len(char))
    dna+=char[rnd]  
  return dna

#Retorna cps copias
#do dnai, cada uma
#com probabilidade
#pmut de mutacao em
#uma letra
def sncopy(dnai,cps,pmut):
  copies=[None]*cps
  for i in range(cps):
    copy=list(dnai)
    for j in range(len(dnai)):
      if random()<pmut:
        c=floor(random()*len(char))
        copy[j]=char[c]
    copies[i]=''.join(copy)  
  return copies

#Retorna quantas
#letras do dnai cor-
#respondem ao dnaf
def snadap(dnai,dnaf):
  a=0
  for i in range(len(dnai)):
    if dnai[i]==dnaf[i]:
      a+=1
  return a

#De uma lista de dnas
#retorna o mais pare-
#cido com o dnaf e
#nivel de adaptacao
def snbest(copies,dnaf):
  adap=0
  for i in range(len(copies)):
    a=snadap(copies[i],dnaf)
    if a>adap:
      adap=a
      best=copies[i]
  return (best,adap)

#Renderiza na tela
#o dna e seu nivel de
#adaptacao
def display(dna,adapt):
  clear_screen()
  draw_string(0,85,
              dna+' '+str(adapt)+'/'+str(len(dna)),
              (0,0,0),
              'large')
  show_screen()