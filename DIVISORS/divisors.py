from math import *

#Retorna uma lista 
#com True nos indices 
#primos e False nos 
#indices compostos
#de 0 a max
def isprime(max):
  len=max+1
  p=[None]*(len)  
  p[0]=False
  p[1]=False
  for i in range(2,len):
    p[i]=True
  i=2 
  while i*i<=max:
    for j in range(2*i,len,i):
      p[j]=False
    i+=1  
  return p

#Retorna a sequencia
#de primos anteriores
#ao numero n para n
#composto, e ate n
#para n primo
def seqprim(n):
  ip=isprime(n)
  p=[]  
  for i in range(len(ip)):
    if ip[i]:
      p.append(i)
  return p

#Retorna uma lista
#com os fatores
#primos de n em ordem
#crescente
def factors(n):
  p=seqprim(floor(sqrt(n)))
  step=0
  f=[]
  step+=1  
  for i in range(len(p)):
    while n%p[i]==0:   
      f.append(p[i])
      n/=p[i]
      step+=2
    step+=1
  if len(f)==0:
    f.append(n)
    step+=1
  return [f,step]

#Implementa o metodo
#tradicional para
#achar os divisores
#de n
def traddiv(n):
  fac=factors(n)
  f=fac[0]
  step=fac[1]
  dn=[1]
  step+=1
  for i in range(len(f)):
    for j in range(len(dn)):
      d=f[i]*dn[j]
      step+=1      
      if not d in dn:
        dn.append(d)
        step+=1
  return [dn,step]

#Implementa um metodo
#de divisao sucessiva
#para achar os
#divisores de n
def succdiv(n):
  step=0
  dn=[1,n]    
  i=2
  step+=2
  while i*i<=n:
    if n%i==0:
      dn.append(i)
      dn.append(n//i)
      step+=2
    i+=1
    step+=1
  return [dn,step]

def propdiv(n):
  step=0
  f=factors(n)
  dn=[1,n,f[0],n//f[0]]
  m=f[0]
  for i in range(1,len(f)):
    if f[i]==f[i-1]:
      m*=f[i]
      if m*m<=n:
        dn.append(m)
        dn.append(n//m)
    else:
      d=f[i-1]*f[i]
      if d*d<=n:
        dn.append(d)
        dn.append(n//d)
      m=f[i]
      dn.append(m)
      dn.append(n//m)   
    step+=1
  return [dn,step]
