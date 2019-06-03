from prettytable import PrettyTable

x = PrettyTable()
a = ["1", "2", "3", "4", "5"]

leng = len(a)
print(leng)

for i in range(len(a)):	
	x.add_column(a[i], [])
	
print(x)