from particle import *

N=10
a=300
d=10
v=5

t=0
while N>1:
  s=stats(N,a,d,v)
  print("T =",s[1])
  t+=s[1]
  print("t =",t)
  N-=1