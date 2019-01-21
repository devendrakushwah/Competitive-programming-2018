import math
t=int(input())
while(t>0):
    t-=1
    n=int(input())
    print(math.ceil(math.log(n,2)))