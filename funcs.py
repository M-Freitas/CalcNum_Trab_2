###############################################################
#AUTOR: MARCOS VINICIUS FREITAS PINTO
#INSTITUIÇÃO: UNIVERSIDADE FEDERAL DO CEARÁ
#CURSO: ESTATÍSTICA
#CONTATO: marcos.freitasp@alu.ufc.br
###############################################################
#coding:utf-8
import numpy as np
from ptables import prettytable

#FUNÇÃO PARA LEITURA DOS DADOS EM ARQUIVO
def read_Matriz(arquivo):
	return [tuple([float(num) for num in line.split(';')]) for line in arquivo]

#FUNÇÃO PARA TRANSFORMAR A MATRIZ TUPLA EM LISTA
def transf_List(matriz):
	matriz_tmp = list(matriz)
	for i in range(len(matriz)):
		matriz_tmp[i] = list(matriz[i])	
	
	return matriz_tmp

#FUNÇÃO PARA MOSTRAR OS DADOS DA MATRIZ
def show_Matriz(matriz):
	for i in range(len(matriz)):
		
		for j in range(len(matriz[0])):
		
			if j == ((len(matriz[0]) - 1)):
				print("%7.3f " %matriz[i][j])
		
			else:
				print("%7.3f " %matriz[i][j], end = " ")

#FUNÇÃO PARA ESCREVER OS DADOS NO ARQUIVO DE RESULTADOS
def write_Matriz(matriz, vetor, res_Cramer, res_Gauss, res_GJordan,res_Final, determs, param_A):
	arq_res = open('res_Sistema.txt', 'a')
	##########
	arq_res.write("---------------------------------------------------------------------\nMatriz do Sistema:\n\n")
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			arq_res.write("%7.3f " %matriz[i][j])
		arq_res.write("\n")
	
	arq_res.write("\nVetor Independente:\n\n")
	for i in range(len(vetor[0])):
		arq_res.write("%7.3f " %vetor[0][i])
	arq_res.write("\n---------------------------------------------------------------------\n\n")
	
	table_det = prettytable.PrettyTable()
	table_det.field_names = ["Determinante do Sistema pelo Método de Cramer"]
	table_det.align["Determinante do Sistema pelo Método de Cramer"] = 'l'
	table_det.add_row(["Determinante do sistema: %0.3f\n" %determs[0]])
	for i in range(1, len(determs)):
		table_det.add_row(["Determinante do sistema trocando a %dª pelo vetor independente: %0.3f\n" %(i, determs[i])])
	arq_res.write(str(table_det))
	arq_res.write("\n\n--------------------------------------------------------------------------\n\n")

	table_res = prettytable.PrettyTable()
	table_res.title = "----------------- Resultado dos Métodos -----------------"
	table_res.field_names = ["Variável", "Parâm. A","Cramer", "Gauss", "Gauss-Jordan","Amplitude"]

	if len(res_Cramer) == len(res_Gauss) == len(res_GJordan):
		for i in range(len(res_Cramer)):
			table_res.add_row(["D_{%d}" %(i + 1),"%0.3f" %param_A ,"%0.3f" %(res_Cramer[i]), "%0.3f" %(res_Gauss[i]), "%0.3f" %(res_GJordan[i]), "%0.3f" %res_Final[i]])

	arq_res.write(str(table_res))
	arq_res.write("\n\n---------------------------------------------------------------------\n\n")
	arq_res.close()


#FUNÇÃO PARA NÃO ACEITAR VALORES MENORES OU IGUAIS A ZERO
def dif_Zero(var):
	var_tmp = float(input("\nDigite um valor para o %s: " %str(var)))
	while var_tmp <= 0:
		var_tmp = float(input("\nDigite um valor para o %s MAIOR QUE ZERO: " %var))

	return var_tmp

#FUNÇÃO PARA SABER SE A MATRIZ É QUADRADA
def quad_Matriz(matriz):
	equals = True
	major = 0
	count = 0
	for i in range(len(matriz)):
		count += 1
		if (len(matriz[0]) ==  len(matriz[i])):
			continue
		else:
			equals = False
			major = i
	if (count != len(matriz)):
		equals = False
		
	return equals, major

#FUNÇÃO PARA TRANSFORMAR A MATRIZ EM TRIANGULAR SUPERIOR
def triang_Matriz(matriz_tmp, vetor_tmp, gauss):
	mod = 0
	for i in range(len(matriz_tmp) - 1):

		if matriz_tmp[i][i] == 0: #VALOR DA DIAGONAL IGUAL A ZERO
			lin = i + 1
			
			for k in range(lin, len(matriz_tmp)):
				if matriz_tmp[k][i] != 0:
				
					for j in range(len(matriz_tmp)):
						tmp = matriz_tmp[i][j]
						matriz_tmp[i][j] = matriz_tmp[k][j]
						matriz_tmp[k][j] = tmp
					mod += 1
			
		if matriz_tmp[i][i] != 0: #VALOR DA DIAGONAL DIFERENTE DE ZERO
			lin = i
			
			for k in range((lin + 1), len(matriz_tmp)):
				fct = -1.0 * (matriz_tmp[k][i] / matriz_tmp[i][i])
				for j in range(len(matriz_tmp)):
					matriz_tmp[k][j] = (fct * matriz_tmp[i][j])+ matriz_tmp[k][j]
				
				if gauss == 1:
					vetor_tmp[0][k] = (fct * vetor_tmp[0][i]) + vetor_tmp[0][k]
				
	if gauss != 1:					
		return matriz_tmp, mod
	else:
		return matriz_tmp, mod, vetor_tmp

#FUNÇÃO PARA TROCAR A COLUNA DESEJADA DA MATRIZ PELO VETOR INDEPENDENTE
def troca_Coluna(matriz, vetor, col):
	for i in range(len(matriz)):
		matriz[i][col] = vetor[0][i]
	
	return matriz

#FUNÇÃO PARA CALCULAR O DETERMINANTE DA MATRIZ
def determ_Matriz(matriz, vetor, det_OG):
	determs = np.ones(len(matriz) + 1)

	if det_OG:
		(matriz_tmp, mod) = triang_Matriz(transf_List(matriz),[], 0)
		for i in range(len(matriz_tmp)):
			determs[0] *= matriz_tmp[i][i]
		
		if determs[0] != 0: 
			det_OG = False

	if det_OG == False:
		
		for i in range(len(matriz)):	
			(matriz_tmp, mod) = triang_Matriz(troca_Coluna(transf_List(matriz), vetor, i), [], 0)
			
			for j in range(len(matriz_tmp)):
				determs[(i + 1)] *= matriz_tmp[j][j]
	
	for i in range(len(determs)):
		if determs[i] == -0.0:
			determs[i] = 0

		elif (mod % 2) != 0:
			determs[i] = -1 * determs[i]
	
	return determs

def subs_Retroativa(matriz, vetor):
	leng = len(matriz)
	res = np.zeros(leng)
	res[leng - 1] = vetor[0][leng - 1] / matriz[leng - 1][leng - 1]
	for i in range(leng - 2, -1, -1):
		soma = 0
		for j in range(i + 1, leng):
			soma = soma + matriz[i][j] * res[j]		
			
		res[i] = (vetor[0][i] - soma)/ matriz[i][i]	
		if res[i] == -0.0:
			res[i] = 0


	return res

#FUNÇÃO PARA CALCULAR OS VALORES DAS VARIAVEIS PELO METODO DE CRAMER
def Cramer(determs):
	varvs = np.zeros(len(determs) - 1)
	for i in range(len(determs) - 1):
		varvs[i] = determs[i + 1]/determs[0]
		if varvs[i] == -0.0:
			varvs[i] = 0

	return varvs

#FUNÇÃO PARA CALCULAR OS VALORES DAS VARIAVEIS PELO METODO DE GAUSS
def Gauss(matriz, vetor):
	vetor_tmp = transf_List(vetor)
	(matriz_tmp, mod, vetor_tmp) = triang_Matriz(transf_List(matriz), vetor_tmp, 1)
	res = subs_Retroativa(matriz_tmp, vetor_tmp)	

	return res

#FUNÇÃO PARA CALCULAR OS VALORES DAS VARIAVEIS PELO METODO DE GAUSS-JORDAN
def Gauss_Jordan(matriz, vetor):
	mod = 0
	matriz_tmp = transf_List(matriz) 
	vetor_tmp = transf_List(vetor)
	res = np.zeros(len(matriz))
	
	for i in range(len(matriz)):
		if matriz_tmp[i][i] == 0:
			for j in range(len(matriz_tmp)):
				tmp = matriz_tmp[i][j]
				matriz_tmp[i][j] = matriz_tmp[k][j]
				matriz_tmp[k][j] = tmp
			mod += 1
		
		if matriz_tmp[i][i] != 0:
			lin = i
			for j in range(lin + 1, len(matriz)):
				matriz_tmp[i][j] = matriz_tmp[i][j]/matriz_tmp[i][i]
			
			vetor_tmp[0][i] = vetor_tmp[0][i]/matriz_tmp[i][i]
			matriz_tmp[i][i] = 1
			
			for k in range(len(matriz)):
				if i != k:
					for j in range(lin + 1, len(matriz)):
						matriz_tmp[k][j] = matriz_tmp[k][j] - (matriz_tmp[k][i] * matriz_tmp[i][j])
					vetor_tmp[0][k] = vetor_tmp[0][k] - (matriz_tmp[k][i] * vetor_tmp[0][i])
					matriz_tmp[k][i] = 0 	
	
	for i in range(len(vetor_tmp[0])):
		res[i] = vetor_tmp[0][i]
		
		if res[i] == -0.0:
			res[i] = 0
	return res

#FUNÇÃO PARA CALCULAR O VALOR DOS DESLOCAMENTOS DOS PENDULOS
def res_Final(res_Cramer, res_Gauss, res_GJordan, param_A):
	res_tmp = []

	if len(res_Cramer) == len(res_Gauss) == len(res_GJordan):
		for i in range(len(res_Cramer)):
			res_tmp.append(res_Gauss[i] * param_A)

	return res_tmp
