#proper divisors
def get_proper_divisors(n):
  l1 = [1]
  i = 2
  while(i*i <= n):

    if n%i == 0:
      l1.append(i)
      l1.append(n/i)
    i = i + 1

  return l1


#check if amicable
def is_amicable(n):
  l1 = get_proper_divisors(n)
  n1 = sum(l1)
  #print n1
  l2 = get_proper_divisors(n1)
  n2 = sum(l2)

  if n1!= n and n2 == n:
    print n1, l1, "  ", n2, l2
    return True

  return False


print is_amicable(220)

s1 = 0
for i in range(1, 10001):
  if is_amicable(i):
    print i
    s1 = s1 + i

print s1
