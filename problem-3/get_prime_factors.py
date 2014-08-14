def get_prime_factors(n):

  k = n
  i = 2
  p_f = []

  while (True):

    if k == i and k!= n:
      p_f.append(i)
      break

    if k % i == 0:
      p_f.append(i)
      k = k / i
    else:
      i = i + 1

  return p_f


n1 = raw_input("Enter the number : ")

print get_prime_factors(int(n1))
