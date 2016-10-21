def get_all_permutations(string):
  if len(string) == 1:
    return [string]

  result = []
  for i, c in enumerate(string):
    for k in get_all_permutations(string[:i] + string[i+1:]):
      result = result + [c + k]

  return result  


print get_all_permutations('abc')
#for i, p in enumerate(get_all_permutations('0123456789')):
#l2 = get_all_permutations('0123')
#print len(l2)
for i, p in enumerate(get_all_permutations('012')):
  if i+1 == 10:
    print p
    break


def factorial(n):
  if n == 1 or n == 0:
    return 1

  return n * factorial(n-1)

print factorial(8)
