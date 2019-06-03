from ptables import prettytable

def read_Matriz(arquivo):
	return [tuple([float(num) for num in line.split(';')]) for line in arquivo]


# arq_open = open('Termos_dpd.txt', 'r')
# arq_openV = open('Termos_idpd.txt', 'r')

arq_open1 = open('res_Matriz.txt', 'a')

param_A = 1
res1 = [1,2,3,4,5,6]
res2 = [1,2,3,4,5,6]
res3 = [1,2,3,4,5,6]
table_res = prettytable.PrettyTable()
table_res.title = "----------------- Resultado dos Métodos -----------------"
table_res.field_names = ["Variável", "Parâm. A","Cramer", "Gauss", "Gauss-Jordan","[D_{n} * A]"]

if len(res1) == len(res2) == len(res3):
	for i in range(len(res1)):
		table_res.add_row(["D_{%d}" %(i + 1),"%0.3f" %param_A ,"%0.3f" %(res1[i]), "%0.3f" %(res2[i]), "%0.3f" %(res3[i]), "%0.3f" %i])

print(table_res)

# matriz = read_Matriz(arq_open)
# vetor = read_Matriz(arq_openV)

# arq_open1.write("Matriz Original:\n")
# for i in range(len(matriz)):
# 	for j in range(len(matriz)):
# 		arq_open1.write("%7.2f " %matriz[i][j])
# 	arq_open1.write("\n")
# arq_open1.write("\nVetor Independente:\n")
# for i in range(len(vetor[0])):
# 	arq_open1.write("%7.2f " %vetor[0][i])
# arq_open1.write("\n")