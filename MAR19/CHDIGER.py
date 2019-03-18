t=int(input())
while(t>0):
  ans=''
  t-=1
  n,d=list(map(str,input().split()))
  darray=[]
  for i in n:
    darray.append(int(i))
  '''
  Don't know what is wrong in this!!!!
  
  m=min(darray)
  mi=darray.index(m)

  if(int(d)<=m):
    ans=d*len(darray)
  else:
    pfix=''
    sfix=''
    for i in range(mi):
      sfix+=d
    for i in range(mi,len(darray)):
      if(darray[i]<int(d)):
        pfix+=str(darray[i])
      else:
        sfix+=d
    ans=pfix+sfix
  print(ans)
'''

  stk=[]

  for i in range(len(darray)):
    if(darray[i]<int(d)):
      while(len(stk)!=0 and stk[-1]>darray[i]):
        stk.pop()
      stk.append(darray[i])
    
  ans=''
  for i in stk:
    ans+=str(i)

  rem = len(darray)-len(ans)

  print(ans+(d*rem))  

    
