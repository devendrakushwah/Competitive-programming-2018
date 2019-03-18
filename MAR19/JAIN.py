t=int(input())
while(t>0):
  t-=1
  n=int(input())
  ar=[]

  #handling input, removing duplicate alphabets and sorting
  for i in range(n):
    inp = list(set(input()))
    inp.sort()
    inp=''.join(inp)
    ar.append(inp)

  all_present='aeiou'

  lookup=dict()
  ans=0

  #sorting according to number of distinct alphabets present
  ar.sort(key = lambda k : len(k))


  

  #loop to count occurence of each string and storing them in distict table
  for i in ar:
    if(i in lookup.keys()):
      lookup[i]+=1
    else:
      lookup[i]=1

  key_list=list(lookup.keys())

  #if "aeiou" is present in input then
  if(ar[-1] == all_present):
    for i in range(lookup[all_present]):
      ans+=i

      
  i=0
  for k in key_list:
    for j in key_list[(i+1):]:
      temp=''.join(sorted(''.join(set(k+j))))
      if temp == all_present:
        ans+= lookup[j]*lookup[k]
    i+=1
    
  print(ans)
      
  
