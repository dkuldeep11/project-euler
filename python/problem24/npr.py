import itertools
perms = itertools.permutations('0123456789')

for i, p in enumerate(perms):
  if i+1 == 1000000:
    print ''.join(p)
    break
