def get_prime_factors(n):
  i = 2
  k = n
  l1 = []

  while(1):
    if i == k or i == n or n==1:
      l1.append(i)
      break

    if k%i == 0:
      l1.append(i)
      k = k/i
    else:
      i = i + 1
    
  return l1


ans = 1
v = []
for i in range(20,2,-1):
  t = get_prime_factors(i)

  flag = False
  for j in t:
    if j!=t[0]:
      flag = True
      break

  if not flag and t[0] not in v:
    ans = ans * i
    v.append(t[0])


print ans        
    
