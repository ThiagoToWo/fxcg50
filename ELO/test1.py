#Simula a copa de
#2022 das oitavas ate
#o campeao
from elo import *

times16=[
["Hol",1970],
["EUA",1776],
["Arg",2138],
["Aus",1790],
["Jap",1912],
["Cro",1952],
["Bra",2012],
["Cor",1811],
["Fra",2110],
["Pol",1710],
["Ing",2015],
["Sen",1743],
["Mar",1848],
["Esp",2033],
["Por",2033],
["Sui",1792]
]

res=[times16,1]
n=len(res[0])

while n >= 2:
  for i in range(0,n,2):
    a=res[0][i]
    b=res[0][i + 1]
    print(a[0],a[1],"x",b[0],b[1])

  print("prob.:","{:.4%}".format(res[len(res)-1]))
  print("---------------------")

  res=bracket(res)
  n=len(res[0])

win=res[0][0]
print(win[0],win[1])
print("prob.:","{:.4%}".format(res[len(res)-1]))