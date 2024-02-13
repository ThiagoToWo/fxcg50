#Definicoes:
#1) resultado:
#[competidores, prob]
#2) competidores:
#[competidor,...]
#3) prob:
#probabilidade do
#resultado
#4) competidor:
#[nome,elo]

#Calcula o jogo entre
#competidores a e b
#e retorna
#[vencedor, prob]
#onde vencedor =
#competidor.
def play(a,b):
  from random import random
  pa=1/(1+10**((b[1]-a[1])/400))
  pb=1-pa
  test=random()
  result=[None]*2
  if test<=pa:
    a[1]+=32*(1-pa)
    b[1]+=32*(0-pb)
    result[0]=[a[0],round(a[1])]
    result[1]=pa
  else:
    a[1]+=32*(0-pa)
    b[1]+=32*(1-pb)
    result[0]=[b[0],round(b[1])]
    result[1]=pb
  return result

#Calcula o resultado
#de uma chave de
#campeonato atraves
#de um resultado
#anterior.
def bracket(res):
  n=len(res[0])
  if n%2!=0:return
  prob=res[1]
  wins=[]
  for i in range(0,n,2):
    result=play(res[0][i],res[0][i+1])
    prob *=result[1]
    wins.append(result[0])   
  return [wins,prob]