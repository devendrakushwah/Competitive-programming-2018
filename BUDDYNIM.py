#BUDDYNIM
for _ in range(int(raw_input())):
  n,m=map(int,raw_input().split())
  ar=map(int,raw_input().split())
  br=map(int,raw_input().split())
  s1=sum(ar)
  s2=sum(br)
  if(s1==1 and s2==1):
    print 'Bob'
  else:
    print 'Alice'
  '''else:
    ar.sort()
    br.sort()
    if((n>m) or (m>n)):
      print 'Alice'
    else:
      i=0
      while(i<n):
        if(ar[i]!=br[i]):
          break
        i+=1
      if(i==n):
        print 'Bob'
      else:
        print 'Alice' '''
  
