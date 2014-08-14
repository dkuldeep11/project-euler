def get_factors(n):
  ans = [1,n]
  i = 2
  k = n

  while True:

    if i>=k:
      break

    if n%i == 0:
      ans.append(i)
      k = n/i
      if k!=i:
        ans.append(k)

    i = i + 1

  return ans


f = get_factors(144)

print f
