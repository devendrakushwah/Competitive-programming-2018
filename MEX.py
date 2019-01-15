t=int(input())
while(t>0):
  t-=1
  n,k=map(int,input().split())
  s=list(map(int,input().split()))
  s.sort()
  ans=s[0]
  for i in range(1,n):
    diff=s[i]-s[i-1]
    if(diff>k or k==0):
      ans=s[i-1]+k+1
      k=0
      break
    k=k-diff
  print(ans)
