def product(c,k,m):
    ans=0
    #c.sort(reverse=True)
    for i in range(m):
        ans+=c[i]*k[i]
    return ans

n,m=list(map(int,input().split()))
c=list(map(int,input().split()))
k=list(map(int,input().split()))
if(n<=m):
    #c.sort(reverse=True)
    #k.sort(reverse=True)
    ans=0
    for i in range(n):
        ans+=c[i]*k[i]
    print(ans)
else:
    #k.sort(reverse=True)
    ans=0
    l=n%m
    for i in range(n-m):
        ans=max(ans,product((c[i:i+m]),k,m))
        #print(ans)
    print(ans)