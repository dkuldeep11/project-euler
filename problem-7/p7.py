#!/usr/bin/python

#sum of squares of 1st 100 numbers
import math

def isPrime(n):
        i = 2
        while ( i <= math.sqrt(n)):
                if ( n % i == 0):
                        return False
                else:
                        i = i + 1

        return True

i = 2

n1 = 10001
c = 0

while (True):
        if isPrime(i):
                c = c + 1
                if (c == n1):
                        break
        i = i + 1


print "prime no ", n1, " = ", i
