from random import *
v1=10
v2=10
danos=[
[[2,2],[0,0],[0,0],[0,2],[1,2]],
[[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0]],
[[2,0],[0,0],[0,0],[0,0],[0,0]],
[[2,1],[0,1],[0,0],[0,0],[1,1]]
]
act=[
["AA\t\t\tAA","AA\t\t\tGA","AA\t\t\tES","AA\t\t\tGB","AA\t\t\tAB"],
["GA\t\t\tAA","GA\t\t\tGA","GA\t\t\tES","GA\t\t\tGB","GA\t\t\tAB"],
["ES\t\t\tAA","ES\t\t\tGA","ES\t\t\tES","ES\t\t\tGB","ES\t\t\tAB"],
["GB\t\t\tAA","GB\t\t\tGA","GB\t\t\tES","GB\t\t\tGB","GB\t\t\tAB"],
["AB\t\t\tAA","AB\t\t\tGA","AB\t\t\tES","AB\t\t\tGB","AB\t\t\tAB"]
]
img=[
["  X<>X\n  |  |\n  |  |","  O>[O\n  |  |\n  |  |","  O->  O\n  |   /\n  |  |","  O->X\n  | [|\n  |  |","  O->X\n  X<-|\n  |  |"],
["  O]<O\n  |  |\n  |  |","  O][O\n  |  |\n  |  |","  O]   O\n  |   /\n  |  |","  O] O\n  | [|\n  |  |","  O] O\n  X<-|\n  |  |"],
["O  <-O\n \\   |\n  |  |","O   [O\n \\   |\n  |  |","O      O\n \\    /\n  |  |","O    O\n \\  [|\n  |  |","O    O\n \\ <-|\n  |  |"],
["  X<-O\n  |] |\n  |  |","  O [O\n  |] |\n  |  |","  O    O\n  |]  /\n  |  |","  O  O\n  |][|\n  |  |","  O  O\n  |]<|\n  |  |"],
["  X<-O\n  |->X\n  |  |","  O [O\n  |->X\n  |  |","  O    O\n  |-> /\n  |  |","  O  O\n  |>[|\n  |  |","  O  O\n  X<>X\n  |  |"],
]

while v1>0 and v2>0:
  print("1 - ataque alto")
  print("2 - guarda alta")
  print("3 - esquiva")
  print("4 - guarda baixa")
  print("5 - ataque baixo")
  a1=int(input("Sua escolha: "))
  while a1<1 or a1>5:
    print("1 - ataque alto")
    print("2 - guarda alta")
    print("3 - esquiva")
    print("4 - guarda baixa")
    print("5 - ataque baixo")
    a1=int(input("Sua escolha: "))
    
  a2=randint(1,5)
  
  a=a1-1
  b=a2-1
  v1-=danos[a][b][0]
  v2-=danos[a][b][1]
    
  print(img[a][b])
  print("--------")
  print("v1:",v1,"\tv2:",v2)
  print(act[a][b])
  input()