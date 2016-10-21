#!/usr/bin/python

import math


a = b = c = 0
s = 1000
f = False

a = 1
while ( a < s/3 ):
        b = a
        while ( b < (s / 2)):
                c = s - a - b
                if ( a * a + b * b == c * c):
                        f = True
                        break
                b = b + 1

        if f:
                break

        a = a + 1


print a, b, c , (a * b * c)

