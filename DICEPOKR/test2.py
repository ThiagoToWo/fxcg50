#Executa o jogo dice
#poker n vezes e im-
#prime quantas vezes
#saiu cada resultado
#em %
from dicepokr import *

d=[0,0,0,0,0]
f=[0,0,0,0,0,0,0]
fv=0
fr=0
st=0
fh=0
th=0
p2=0
p=0
no=0

n=30000

for i in range(n):
  play(d,f)
  if ispair(f):
    p+=1
  elif is2pair(f):
    p2+=1
  elif isthree(f):
    th+=1
  elif isfullhouse(f):
    fh+=1
  elif isstraight(f):
    st+=1
  elif isfour(f):
    fr+=1
  elif isfive(f):
    fv+=1      
  else:
    no+=1
  d=[0,0,0,0,0]  
  f=[0,0,0,0,0,0,0]
  
print("pair:","{:%}".format(p/n))
print("2 pair:","{:%}".format(p2/n))
print("three:","{:%}".format(th/n))
print("full house:","{:%}".format(fh/n))
print("straight:","{:%}".format(st/n))
print("four:","{:%}".format(fr/n))
print("five:","{:%}".format(fv/n))
print("no value:","{:%}".format(no/n))