t=int(input())
while(t>0):
  t-=1
  n=int(input())
  s=[]
  for i in range(n):
    s.append(input())
  mtx=[[0 for i in range(26)] for j in range(n)]
  for i in range(n):
    for e in s[i]:
      mtx[i][ord(e)-97]+=1
  ans=[1 for i in range(26)]
  for i in range(26):
    for j in range(n):
      if(mtx[j][i]==0):
        ans[i]=0
        i+=1
        break
  print(sum(ans))
