t=int(input())
while(t>0):
    t-=1
    lhs,rhs=list(map(str,input().split("=")))
    ans=eval(lhs)
    if(ans == int(rhs)):
        print("Valid Equation")
    else:
        print("Invalid Equation")