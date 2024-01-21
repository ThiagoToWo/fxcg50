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
  f=[]
  p=2
  
  while p<=n:
    while n%p==0:
      f.append(p)
      n/=p
    
    if p==2:
      p=3     
    else:
      p+=2
      
  return f
