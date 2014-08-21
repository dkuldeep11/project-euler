from num2words import num2words

num = {1 : 'one', 
       2 : 'two',
       3 : 'three',
       4 : 'four',
       5 : 'five',
       6 : 'six',
       7 : 'seven',
       8 : 'eight',
       9 : 'nine',
       10 : 'ten',
       11 : 'eleven',
       12 : 'twelve',
       13 : 'thirteen',
       14 : 'fourteen',
       15 : 'fifteen',
       16 : 'sixteen',
       17 : 'seventeen',
       18 : 'eighteen',
       19 : 'nineteen',
       20 : 'twenty',
       30 : 'thirty',
       40 : 'forty',
       50 : 'fifty',
       60 : 'sixty',
       70 : 'seventy',
       80 : 'eighty',
       90 : 'ninety',
       100 : 'onehundred',
       1000 : 'onethousand',
       0 : ''
}


def getWordFromNum(n):
  if n in num:
    return num[n]
  else:
    n1 = ''
    if len(str(n)) == 2:
      n1 = n1 + num[(n/10)*10]
      n1 = n1 + num[n%10]
    else:
      n1 = n1 + num[n/100]
      n1 = n1 + 'hundred'
      temp = n%100
      if temp == 0:
        return n1

      n1 = n1 + 'and'
      if temp in num:
        n1 = n1 + num[temp]
      else:
        n1 = n1 + num[(temp/10)*10]
        n1 = n1  + num[temp%10]

    return n1
      
sum = 0
for i in range(1,1001):
  sum = sum + len(getWordFromNum(i))

print sum
