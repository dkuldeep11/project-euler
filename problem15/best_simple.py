g = 20;
paths = 1;

p = 1 
for i in range( 1, g+1):
  t = (2*g + 1 - i)/i
  p = p * t

print p

def getnCr(n, r):
  p = 1
  for i in range(1, r+1):
    p = p * (n + 1 - i)
    p = p/i

  return p


print getnCr(40,20)
