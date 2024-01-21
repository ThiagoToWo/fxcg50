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

#Implementa o método
#tradicional para
#achar os divisores
#de n
def traddiv(n):
  step=0
  f=factors(n)
  dn=[1]
  for i in range(len(f)):
    for j in range(len(dn)):
      d=f[i]*dn[j]      
      if not d in dn:
        dn.append(d)
      step+=1
  print(step)
  return dn

#Implementa um método
#melhor para achar os
#divisores de n
def newdiv(n):
  step=0
  dn=[1,n]    
  i=2
  while i*i<=n:
    if n%i==0:
        dn.append(i)
        dn.append(n//i)
    i+=1
    step+=1
  print(step)
  return dn