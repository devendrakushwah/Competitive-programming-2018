from decimal import *
getcontext().prec=105
t=int(input())
while(t>0):
    t-=1
    a,b=list(map(int,input().split()))
    c=str(Decimal(a)/Decimal(b))
    if(len(c)==3 and c[-1]=='0'):
        print(c[0])
    else:
        print(c[:103])
    print(len(c))
