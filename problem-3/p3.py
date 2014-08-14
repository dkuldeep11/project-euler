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


def get_max_prime_factor(n):

  k = n
  i = 2

  max = 2

  while (True):

    if k == i and k!= n:
      if i > max:
        max = i
      break

    if k % i == 0:
      if i > max:
        max = i
      k = k / i
    else:
      i = i + 1

  return max


n1 = raw_input("Please enter the number: ")

#print get_prime_factors(int(n1))
print get_max_prime_factor(int(n1))








