

def fib(n):
  if n == 0 or n == 1:
    return 1

  return fib(n-1) + fib(n-2)


n = 1
sum = 0

for n in range(1, 11):
  print fib(n)


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors


#pfs = prime_factors(600851475143)
pfs = prime_factors(1000)
largest_prime_factor = max(pfs)

print largest_prime_factor
print pfs
