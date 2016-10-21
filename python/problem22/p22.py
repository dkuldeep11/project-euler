def get_count(name):
  score = 0
  for c in name:
    score  = score + ord(c) - 64

  return score
    

names = open("names.txt").readlines()

l1 = names[0].split(",")

l1.sort()

print len(l1)

s = 0
for i in range(0,len(l1)):
  
  c1 = get_count(l1[i].replace('"',''))
  #print l1[i]
  if l1[i] == '"ZULMA"':
    print i+1
  s = s + c1*(i+1)

 

print s

