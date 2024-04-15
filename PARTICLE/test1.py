from particle import *
from random import *
from math import *

N=5
a=5
r=1
v=10
e=elements
time=0
for i in range(N):
  p=particle.copy()
  x=r+random()*(a-r)
  y=r+random()*(a-r)
  z=r+random()*(a-r)
  vx=-v+random()*2*v
  rem=(v**2-vx**2)**.5
  vy=-rem+random()*2*rem
  vz=(rem**2-vy**2)**.5
  set(p,x,y,z,r,vx,vy,vz)
  e.append(p)
while len(e)>1:
  i=0
  while i<len(e):
    update(e[i])
    bounds(e[i],a)
    j=i+1
    while j<len(e):
      if collided(e[i],e[j]):
        join(e[i],e[j])
      j+=1
    i+=1
  time+=1
print(e)
print(time)  