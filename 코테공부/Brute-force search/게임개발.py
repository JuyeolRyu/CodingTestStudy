{\rtf1\ansi\ansicpg949\deff0\nouicompat\deflang1033\deflangfe1042{\fonttbl{\f0\fnil\fcharset129 \'b8\'bc\'c0\'ba \'b0\'ed\'b5\'f1;}}
{\*\generator Riched20 10.0.17763}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs20\lang18 field = []\par
ans = 1\par
direction_set = \{0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]\}\par
check =[False,False,False,False]\par
\par
n, m = map(int, input().split())\par
x,y,direction = map(int, input().split())\par
\par
for i in range(n):\par
  tmp = []\par
  for j in map(int,input().split()):\par
    tmp.append(j)\par
  field.append(tmp)\par
\par
#\'bf\'de\'c2\'ca \'c3\'a3\'b1\'e2,\'b9\'e6\'c7\'e2 \'bf\'de\'c2\'ca\'c0\'b8\'b7\'ce \'ba\'af\'b0\'e6\par
\par
\par
while(True):\par
  direction = (direction + 3)%4\par
  left = direction_set[ direction ]\par
\par
  if( field[x + left[0]][y + left[1]] == 0):\par
    check =[False,False,False,False]\par
    field[x][y] = -1\par
    x += left[0]\par
    y += left[1]\par
    ans += 1\par
  else:\par
    check[direction] = True\par
\par
  if False not in check:\par
    direction = (direction + 2)%4\par
    back = direction_set[direction]\par
    if(field[x + back[0]][y+ back[1]] == 1):\par
      print(ans)\par
      break\par
    else:\par
      x += back[0]\par
      y += back[1]\par
}
 