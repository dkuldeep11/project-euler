#find total days in 20th century
total_days = 0

def isLeapyear(n):
  if n%100 == 0 and n%400 == 0:
    return True
  elif n%4 == 0:
    return True
  else:
    return False

for i in range(1901, 2001):
  if isLeapyear(i):
    total_days = total_days + 366
  else:
    total_days = total_days + 365

#print total_days

#find sunday numbers
sundays = []
k = 0
s = 6
while(s<=total_days):  
  s = 7*k + 6
  k = k + 1
  sundays.append(s)

#print len(sundays)


#find 1st day month numbers
first_days_month = []
d1 = 1
first_days_month.append(d1)
for year in range(1901, 2001):
  for m in range(1,13):
    if ( m in [1, 3, 5, 7, 8, 10, 12]):
      d1 = d1 + 31
    elif m == 2:
      if isLeapyear(year):
        d1 = d1 + 29
      else:
        d1 = d1 + 28
    else:
      d1 = d1 + 30

    first_days_month.append(d1)

  
#print len(first_days_month) 

#check for matches, match count is the answer
cnt = 0
for s in sundays:
  if s in first_days_month:
    #print s
    cnt = cnt + 1

print cnt  
