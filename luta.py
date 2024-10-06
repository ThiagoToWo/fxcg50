from random import *

def ctn():
  input('[EXE] continue')
  
pos=['a','b','c','d']
v1=10
e1=10
a1=[None]*e1
v2=10
e2=10
a2=[None]*e2

print('v1:',v1,'- e1:',e1)
print('v2:',v2,'- e2:',e2)
print('Voce tem',e1,'acoes')
print('Digite elas: ')
for i in range(e1):
  #a1[i]=pos[randint(0,3)]
  a1[i]=input('a['+str(i)+']=')

for i in range(e2):
  a2[i]=pos[randint(0,3)]

for i in range(min(e1,e2)):
  print('jogador\t\toponente')
  print('a1:',a1[i],'\t\ta2:',a2[i])
  if a1[i]!=a2[i] and a1[i]!='d' and a2[i]!='d':
    if a1[i]=='a':
      v2=v2-3
      print('v1:',v1,'\t\tv2-3:',v2)
    elif a1[i]=='b':
      v2=v2-2
      print('v1:',v1,'\t\tv2-2:',v2)
    elif a1[i]=='c':
      v2=v2-1
      if i+1<e2:
        a2[i+1]='0'
        print('v1:',v1,'\t\tv2-1:',v2)
        print('Oponente paralizado')

    if v2<=0:
      ctn()
      break

    if a2[i]=='a':
      v1=v1-3
      print('v1-3:',v1,'\tv2:',v2)
    elif a2[i]=='b':
      v1=v1-2
      print('v1-2:',v1,'\tv2:',v2)
    elif a2[i]=='c':
      v1=v1-1
      if i+1<e1:
        a1[i+1]='0'
        print('v1-1:',v1,'\tv2:',v2)
        print('Jogador paralizado')

    if v1<=0:
      ctn()
      break

  ctn()

print('RESUMO')
print('jogador\t\toponente')
print('v1:',v1,'\t\tv2:',v2)
print('a1:',''.join(a1))
print('a2:',''.join(a2))