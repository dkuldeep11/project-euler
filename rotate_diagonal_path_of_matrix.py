
i, j, l = 2, 3, 5

for i1 in range(0, l):
  print i + i1, j + i1


print
print
#we need to use symmetricity to rotate i.e. we just need to iterate half the times of length which is l here

#in 1st iteration we will shift the extreme elements and in 2nd remaining 2
#this also works in generic way i.e. iterate half the times of lenght and deal with 2 elemts at a time which in total orders the total elements in diagonal
for x in range(0,l/2):
  print i+x, j + (l - 1 - x)
  print i+l-1-x, j+l-1-(l-1-x)

if not l%2 == 0:
  print i+l/2, j+l/2

  

