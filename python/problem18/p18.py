import numpy as np

from StringIO import StringIO

ip1 = '''3 0 0 0
7 4 0 0
2 4 6 0
8 5 9 3'''

G = np.loadtxt(StringIO(ip1), dtype='int')

print G.shape
print len(G)

for (x,y), val  in np.ndenumerate(G):
  print x,y, "=>", G[x][y]

def traverse_all(r, c):
  curr = G[r][c]
  if r < len(G) - 1:
    p1 = traverse_all(r+1, c)
    p2 = traverse_all(r+1, c+1)
    #print p1 + p2
    temp = p1 + p2
    return [[curr] + path for path in temp]
  else:
    #print [[curr]]
    return [[curr]]


#print traverse_all(0,0)

#brute force attack

raw_input = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

str1 = ''

for l1 in raw_input.split("\n"):
  c1 = 0
  for i in l1.split(" "):
    str1 = str1 + i + " "
    c1 = c1 + 1

  print c1

  for i in range(0, 15-c1):
    str1 = str1 + " 0"

  str1 = str1 + "\n"

  
print str1
G = np.loadtxt(StringIO(str1), dtype='int')

print G.shape

max = 0

for path in traverse_all(0,0):
  s = 0
  for e in path:
    s = s + e
    
  if s > max:
    max = s

print max  



