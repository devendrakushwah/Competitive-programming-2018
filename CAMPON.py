for _ in range(int(raw_input())):
  d=int(raw_input())
  dp={}
  for i in range(d):
    x,y=map(int,raw_input().split())
    dp[x]=y
  q=int(raw_input())
  for j in range(q):
    dead,req=map(int,raw_input().split())
    s=0
    #print sorted(dp.keys())
    for i in sorted(dp.keys()):
      if(i>dead):
        break
      else:
        s+=dp[i]
    #print 'sum',s
    if(s>=req):
      print 'Go Camp'
    else:
      print 'Go Sleep'
