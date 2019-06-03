




l = [[1,1,1], [1,1,1],[1,1,1]]
leng = len(l)
for i in range(leng - 2, -1, -1):
		sum = 0
		for j in range(i + 1, leng):
			print("J: %d" %j)
		print("I: %d" %i)