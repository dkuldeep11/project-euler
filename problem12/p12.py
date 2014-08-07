def get_factors_len(n):
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

  return len(ans)

j = 1

while True:
  m = j * (j+1) /2
  l = get_factors_len(m)
  print m, "=>", l
  if l > 500:
    print m
    break

  j = j + 1
