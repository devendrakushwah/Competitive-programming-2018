MAX=(10**5)+1
primes=[1]*MAX
pfix=[0]*MAX
def sieve():
  for i in range(2,MAX):
    if(primes[i]):
      for j in range(i*i,MAX,i):
        primes[j]=0
#main
sieve()
n=int(input())
if(n==1 or n==2):
  print('NO')
else:
  s=''
  for i in range(2,n+1):
    if(primes[i]):
      s+=str(i)
      s+=' '
  print(s[:-1])

