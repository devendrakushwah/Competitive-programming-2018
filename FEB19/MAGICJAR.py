t=int(input())
while(t>0):
  t-=1
  n=int(input())
  a=list(map(int,input().split()))
  print(sum(a)-n+1)
