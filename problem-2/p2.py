

def fib(n):
  if n == 0 or n == 1:
    return 1

  return fib(n-1) + fib(n-2)

p = 1
sum = 0

while(True):
  k = fib(p)
  #print p, "=>", k

  if k > 4000000:
    break

  if k%2 == 0:
    sum = sum + k

  p = p + 1
print sum

