n,k,r=list(map(int,input().split()))
ans=0
for i in range(1,n*r):
    k=k-(i*r)
    if(k<0):
        break
    ans += 1
    print(k)
print(n-ans)