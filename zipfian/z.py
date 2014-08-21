s = 0

for i in range(3,118):
  if i%15 == 0:
    s = s + 15
  elif i%5 == 0:
    s = s + 5
  elif i%3 == 0:
    s = s + 3
  else:
    s = s + 1

print s
