n=int(input())
while(n>0):
  n-=1
  s=input()
  '''flag=False
  if((s[:3]=='not') or s[-3:]=='not'):
    flag=True
  else:
    for i in range(5,len(s)-3):
      print(s[i-2:i+1])
      if(s[i-2:i+1]=='not' and s[i-3]==' ' and s[i+1]==' '):
        flag=True
        break'''
  
  if('not' in s.split()):
    print('Real Fancy')
  else:
    print('regularly fancy')
    
