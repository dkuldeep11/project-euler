s1 = '''Zeldin Yaakov, Toby
 Prasad, Jokhan
 Sambayya, Arun
 Gavri, Ankur
 Liu, Alan
 Creed, John
 Vanama, Srikanth
 Schaar, Robert
 Negm, Sally
 Basha, Jahangir
 Wang, Hellya
 Prabhu, Ganesh
 Tsjin, Budiman
 Kok, Jeffrey'''

l1 = s1.split("\n")

print l1

s2 = '''Liu, Alan
 Creed, John
 Vanama, Srikanth
 Schaar, Robert
 Negm, Sally'''

l2 = s2.split("\n")

print l2


for n in l1:
  if n not in l2:
    print n


