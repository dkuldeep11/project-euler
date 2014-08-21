

def isPallindrome(n):
  if str(n) == str(n)[::-1]:
    return True
  return False

max = 1
for i in range(100,1000):
  for j in range(100,1000):
    n = i * j
    if isPallindrome(n) and n > max:
      max = n      

print max


