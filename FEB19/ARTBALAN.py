def solve(s,n):
    freq=[0]*26
    ans=10**9
    for c in s:
        freq[ord(c)-65]+=1
    freq.sort()
    for i in range(1,27):
        if(n%i != 0):
            continue
        x=n/i
        temp=0
        for j in range(26-i):
            temp+=freq[j]
        for j in range(26-i,26,1):
            temp+=abs(freq[j]-x)
        temp = temp / 2
        ans=min(ans,temp)
    return int(ans)

t=int(input())
while(t>0):
    t-=1
    s=input()
    n=len(s)
    print(solve(s,n))