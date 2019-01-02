#since log(a*b)=loga+logb, we have to find only primes in range [1,N]
MAX=(10**6)+1
primes=[1]*MAX
pfix=[0]*MAX
def sieve():
  for i in range(2,MAX):
    if(primes[i]):
      for j in range(i*i,MAX,i):
        primes[j]=0    

#main
q=int(input())
sieve()
for i in range(2,MAX):
  pfix[i]=pfix[i-1]
  if(primes[i]):
    pfix[i]+=1

while(q>0):
  q-=1
  n=int(input())
  print(pfix[n])
