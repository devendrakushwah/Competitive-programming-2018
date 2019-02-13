import math
t=int(input())
while(t>0):
  t-=1
  n,b,a,k=list(map(int,input().split()))
  x=int(n/a)
  y=int(n/b)
  lcm=(a*b)/math.gcd(a,b)
  z=int(n/lcm)
  print(x,y,z)
  if ((x+y)-(2*z))>=k:
    print('Win')
  else:
    print('Lose')
