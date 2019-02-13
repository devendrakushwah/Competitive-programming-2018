t=int(input())
while(t>0):
  t-=1
  n=int(input())
  attack=list(map(int,input().split()))
  defence=list(map(int,input().split()))

  ans=-1

  #for 1st soldier
  if(defence[0]>attack[n-1]+attack[1]):
    if(defence[0]>=ans):
      ans=defence[0]

  #for rest
  for i in range(1,n-1):
    if(defence[i]>(attack[i-1]+attack[i+1])):
      if(defence[i]>=ans):
        ans=defence[i]

  #for last soldier
  if(defence[n-1]>(attack[0]+attack[n-2])):
    if(defence[n-1]>=ans):
      ans=defence[n-1]

  print(ans)
  
