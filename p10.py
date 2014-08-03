# function to check if number is prime

def is_prime(num):
# prime numbers are greater than 1
   # check for factors
   for i in range(2,num/2 + 1):
       if (num % i) == 0:
           #print(num,"is not a prime number")
	   return False
   else:
       #print(num,"is a prime number")
	return True
       
sum = 0
for i in range(2, 2000000):
    n = 0
    if is_prime(i):
	n = i
        sum = sum + n

print sum
