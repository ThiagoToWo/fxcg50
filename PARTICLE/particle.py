from math import *

#Dado a quatidade de
#particulas n, a
#aresta a, o diametro
#d e a velocidade v,
#retorna uma lista
#com a frequencia de
#colisoes f, o perio-
#do entre as colisoes
#t e o livre percurso
#medio l
def stats(n,a,d,v):
  f=sqrt(2)*pi*(n/a**2)*v*d**2
  t=1/f
  l=v*t
  return [f,t,l]
  
#Objeto que guarda as
#caracteristicas de
#uma particula
particle={
  "x":0,
  "y":0,
  "z":0,
  "r":1,
  "vx":0,
  "vy":0,
  "vz":0
}

#Lista de particulas
elements=[]

#Configura a particu-
#la p com sua posicao
#x, y, z, seu raio r
#e sua velocidade vx,
#vy, vz
def set(p,x,y,z,r,vx,vy,vz):
  p["x"]=x
  p["y"]=y
  p["z"]=z
  p["r"]=r
  p["vx"]=vx
  p["vy"]=vy
  p["vz"]=vz

#Atualiza a posicao
#da particula somando
#sua velocidade
def update(p):
   p["x"]+=p["vx"]
   p["y"]+=p["vy"]
   p["z"]+=p["vz"]

#Retorna se a parti-
#cula p1 colidiu com
#p2   
def collided(p1,p2):
  dx=p1["x"]-p2["x"]
  dy=p1["y"]-p2["y"]
  dz=p1["z"]-p2["z"]
  d=(dx**2+dy**2+dz**2)**.5
  return d<=p1["r"]+p2["r"]

#Verifica e atualiza
#a posicao e a velo-
#cidade da particula
#p apos ela colidir
#com os limites do
#cubo de aresta a
def bounds(p,a):
  if p["x"]<p["r"]:
    p["x"]=p["r"]
    p["vx"]=-p["vx"]
  if p["x"]>a-p["r"]:
    p["x"]=a-p["r"]
    p["vx"]=-p["vx"]
  if p["y"]<p["r"]:
    p["y"]=p["r"]
    p["vy"]=-p["vy"]
  if p["y"]>a-p["r"]:
    p["y"]=a-p["r"]
    p["vy"]=-p["vy"]
  if p["z"]<p["r"]:
    p["z"]=p["r"]
    p["vz"]=-p["vz"]
  if p["z"]>a-p["r"]:
    p["z"]=a-p["r"]
    p["vz"]=-p["vz"]

#Une a particula p1
#com p2 apos elas
#colidirem    
def join(p1,p2):
  x=(p1["x"]+p2["x"])/2
  y=(p1["y"]+p2["y"])/2
  z=(p1["z"]+p2["z"])/2
  r=(p1["r"]**3+p2["r"]**3)**(1/3)
  vx=(p1["vx"]+p2["vx"])/2
  vy=(p1["vy"]+p2["vy"])/2
  vz=(p1["vz"]+p2["vz"])/2
  set(p1,x,y,z,r,vx,vy,vz)
  elements.remove(p2)