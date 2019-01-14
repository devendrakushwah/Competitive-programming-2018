n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=''
maxa=a.index(max(a))
minb=b.index(min(b))
for i in range(0,n):
  ans+=str(i)+' '+str(minb)+'\n'
for i in range(0,m):
  if(i!=minb):
    ans+=str(maxa)+' '+str(i)+'\n'
print(ans[:-1])
