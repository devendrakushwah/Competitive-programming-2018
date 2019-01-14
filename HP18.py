#HP18
for _ in range(int(input())):
  n,a,b=list(map(int,input().split()))
  ar=list(map(int,input().split()))
  if(a==b):
    print('BOB')
  else:
    c_bob,c_alice,c_both=0,0,0
    for i in ar:
      if(i%a==0 and i%b==0):
        c_both+=1
      elif(i%a==0):
        c_bob+=1
      elif(i%b==0):
        c_alice+=1
    if(c_both==0):
      if(c_bob>c_alice):
        print('BOB')
      else:
        print('ALICE')
    else:
      if(c_bob>=c_alice):
        print('BOB')
      else:
        print('ALICE')
