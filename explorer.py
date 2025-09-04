from random import *

def mapa(l,h,x,y):
  m=[None]*h
  m[0]=["+"]*l
  for i in range(1,h-1):
    line=[None]*l
    line[0]="+"
    for j in range(1,l-1):
      rnd=random()
      if rnd<0.4:
        line[j]="#"
      elif rnd<0.99:
        line[j]=" "
      else:
        line[j]="$"
    line[l-1]="+"
    m[i]=line
  m[h-1]=["+"]*l  
  m[x][y]="@"
  return m

def render(m,x,y,lc,hc):
  global lm
  global hm
  cx=x-lc//2
  cy=y-hc//2
  d="7-ajuda        mv:"+str(move)+"\n"
  if cx<0:
    cx=0
  if cx+lc>=lm:
    cx=lm-lc
  if cy<0:
    cy=0
  if cy+hc>=hm:
    cy=hm-hc
  for i in range(cy,cy+hc):
    for j in range(cx,cx+lc):
      d+=m[i][j]
    d+="\n"
  print(d,end="")

def update():
  global x
  global y
  global move
  global jogo
  try:
    mv=int(input("?: "))
  except ValueError:
    mv=10  
  if mv==4 and move>0:
    if x-1>=0 and m[y][x-1]!="#":
      m[y][x]="."
      x-=1
      move-=1
      if m[y][x]=="$":
        move+=randint(imin,imax)
      m[y][x]="@"
  elif mv==8 and move>0:
    if y-1>=0 and m[y-1][x]!="#":
      m[y][x]="."
      y-=1
      move-=1
      if m[y][x]=="$":
        move+=randint(imin,imax)
      m[y][x]="@"      
  elif mv==6 and move>0:
    if x+1<len(m[y]) and m[y][x+1]!="#":
      m[y][x]="."
      x+=1
      move-=1
      if m[y][x]=="$":
        move+=randint(imin,imax)
      m[y][x]="@"
  elif mv==2 and move>0:
    if y+1<len(m) and m[y+1][x]!="#":
      m[y][x]="."
      y+=1
      move-=1
      if m[y][x]=="$":
        move+=randint(imin,imax)
      m[y][x]="@"
  elif mv==0:
    print("Fechando o jogo")
    jogo=False
  elif mv==7:
    print("4-move p/ esquerda")
    print("8-move p/ cima")
    print("6-move p/ direita")
    print("2-move p/ baixo")
    print("0-sai do jogo")
    print("$-ganha movimento")
    input("continue")

#medidas do mapa
lm=100
hm=100
#posicao personagem
x=lm//2
y=hm//2
#mapa
m=mapa(lm,hm,x,y)
#movimentos
move=99
#acrescimos min e max
imin=2
imax=30

jogo=True
while jogo:
  render(m,x,y,14,5)
  update()