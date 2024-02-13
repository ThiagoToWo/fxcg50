from divisors import *

n=1000
tdwin=0
sdwin=0
draw=0

for i in range(1,n):
  td=traddiv(i)
  sd=succdiv(i)
  
  if td[1]<sd[1]:
    tdwin+=1
  elif td[1]>sd[1]:
    sdwin+=1
  else:
    draw+=1
  
print("td win:","{:.1%}".format(tdwin/n))
print("sd win:","{:.1%}".format(sdwin/n))
print("draw:","{:.1%}".format(draw/n))