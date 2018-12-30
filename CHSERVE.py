for _ in range(int(raw_input())):
  p1,p2,k=map(int,raw_input().split())
  s=p1+p2
  div=s/k
  mod=s%k
  if(div%2 == 1):
    print 'COOK'
  else:
    print 'CHEF'
