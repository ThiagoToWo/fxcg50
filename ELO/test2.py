#Simula a copa de
#2022 das oitavas ate
#o campeao m vezes e
#conta quantas vezes
#cada time ganhou (%)
from elo import *

winers=[
["Hol",0],
["EUA",0],
["Arg",0],
["Aus",0],
["Jap",0],
["Cro",0],
["Bra",0],
["Cor",0],
["Fra",0],
["Pol",0],
["Ing",0],
["Sen",0],
["Mar",0],
["Esp",0],
["Por",0],
["Sui",0]
]
m=100
for i in range(m):
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

  while n>=2:
    res=bracket(res)
    n=len(res[0])

  win=res[0][0]
  for i in range(len(winers)):
    if win[0]==winers[i][0]:
      winers[i][1]+=1 
   
for i in winers:
  print(i[0],"{:.0%}".format(i[1]/m))