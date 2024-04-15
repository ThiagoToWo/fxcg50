#Retorna o fatorial
#do numero n
def fact(n):
  f=1
  for i in range(2,n+1):
    f*=i
  return f

#Retorna a proxima
#permutacao dos
#elementos da lista a
#na ordem lexicogra-
#fica
def lext(list):
  a=list.copy()
  n=len(a)
  
  j=n-2
  while a[j]>=a[j+1]:
    j-=1
  if j==-1:
    return a
  
  l=n-1
  while a[j]>=a[l]:
    l-=1
  aux=a[j]
  a[j]=a[l]
  a[l]=aux
  
  k=j+1
  l=n-1
  while k<l:
    aux=a[k]
    a[k]=a[l]
    a[l]=aux
    k+=1
    l-=1
  
  return a

#Retorna uma matriz
#em que cada linha e
#uma permutacao da
#lista a
def permut(a):
  a.sort()
  n=len(a)
  fn=fact(n)
  p=[a]
  for i in range(1,fn):
    p.append(lext(p[i-1]))
  return p

#Imprime cada permu-
#tacao da lista a  
def print_pmt(a):
  a.sort()
  n=len(a)
  fn=fact(n)
  p=[a]
  print(p[0])
  for i in range(1,fn):
    p.append(lext(p[i-1]))
    print(p[i])