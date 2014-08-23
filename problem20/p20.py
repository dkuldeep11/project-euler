def fact(num):
  if num == 1 or num == 0:
    return num
  
  return num * fact(num-1)


#get the factorial
n1 = fact(100)
#print n1
#add the numbers - answer
s = 0
for d in str(n1):
  s = s + int(d)

print s
