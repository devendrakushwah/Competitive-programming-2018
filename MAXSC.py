''' greedy approach :-
    start with maximum of the last list
    then find the maximum element but it should be less than previous maximum
'''

for _ in range(int(raw_input())):
  n=int(raw_input())
  ar=[]
  for i in range(n):
    ar.append(map(int,raw_input().split()))
  ans=max(ar[-1])
  pm=max(ar[-1])
  flag=True
  for i in range(n-2,-1,-1):
    m=0
    cm=0
    for j in ar[i]:
      if(j>cm and j<pm):
        cm=j
    if(cm==0):
      flag=False
      break
    else:
      ans+=cm
      pm=cm
    #print 'cm',cm
  if(flag):
    print ans
  else:
    print -1
