from casioplot import *
from random import *

xmax=360
back=0
step=2
cash=100
play=True

while play:
  x1=0
  y1=70
  x2=0
  y2=95
  x3=0
  y3=120

  print("Voce tem R$",cash)
  bet=float(input("Valor da aposta:"))
  while bet>cash or bet<=0:
    bet=float(input("Valor da aposta:"))
  horse=int(input("Cavalo (1,2,3):"))
  while horse>3 or horse<1:
    horse=int(input("Cavalo (1,2,3):"))
  
  while x1<xmax and x2<xmax and x3<xmax:
    clear_screen()
    for i in range(y1-15,y3+25):
      set_pixel(xmax,i)
    draw_string(x1,y1,"1",(255,0,0),"small")
    draw_string(x2,y2,"2",(0,255,0),"small")
    draw_string(x3,y3,"3",(0,0,255),"small")
    x1+=back+int(random()*step)
    x2+=back+int(random()*step)
    x3+=back+int(random()*step)
    show_screen()

  if x1>=xmax:
    draw_string(10,0,"O cavalo 1 venceu")
    if horse==1:
      cash+=bet
    else:
      cash-=bet
  elif x2>=xmax:
    draw_string(10,0,"O cavalo 2 venceu")
    if horse==2:
      cash+=bet
    else:
      cash-=bet      
  else:
    draw_string(10,0,"O cavalo 3 venceu")
    if horse==3:
      cash+=bet
    else:
      cash-=bet
   
  for i in range(50000):
    show_screen()
  if cash==0:
    play=False
      
print("Voce tem R$",cash)  
input("Fim do jogo")    