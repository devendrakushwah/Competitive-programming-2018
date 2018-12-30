for _ in range(int(raw_input())):
  n=int(raw_input())-1
  div=n//26
  mod=n%26
  #print div,mod
  if(mod<2):
    print str(2**div)+' 0 0'
  elif(mod<10):
    print '0 '+str(2**div)+' 0'
  else:
    print '0 0 '+str(2**div)
