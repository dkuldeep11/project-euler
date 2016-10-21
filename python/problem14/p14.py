n1 = 13

chain_len = 0
ans = 1

for i in range(1, 1000000):
    #print "FOR ", i
    n1 = i
    temp_len = 0
    while n1 != 1:
	if n1%2 == 0:
		n1 = n1/2
	else:
		n1 = 3*n1 + 1

	temp_len = temp_len + 1
	#print temp_len, " => ", n1

    if temp_len > chain_len:
        chain_len = temp_len
        ans = i


print "MAX Chain length generating number = =", ans
