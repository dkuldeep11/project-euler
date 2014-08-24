#function: to get proper factors of a number
def get_proper_factors(n):
  l1 = [1]
  i = 2
  while(i * i <= n):
    if n%i == 0:
      l1.append(i)
      if i*i != n:
        l1.append(n/i)
      
    i = i + 1

  return l1


#function: is abundant(it is called abundant if this sum of factors exceeds n) number
def is_abundant(n):
  factors = get_proper_factors(n)
  if sum(factors) > n:
    return True
  
  return False


#get abundant list
abundant_list = []
for i in range(1, 28124):
  if is_abundant(i):
    abundant_list.append(i)

  
#print abundant_list 


#get sum pairs of a number
def get_sum_pairs(n):
  l1 = []
  for i in range(1, n/2 + 1):
    l2 = [i, n-i]
    l1.append(l2) 
  return l1

    
#find the solution
s1 = 0
temp = []
for i in range(1, 28124):
  sum_pairs = get_sum_pairs(i)
  flag = True
  for p in sum_pairs:
    if is_abundant(p[0]) and is_abundant(p[1]):
      flag = False
      break
    
  if flag:
    s1 = s1 + i

print s1
      
