import numpy as np

def read_Matriz(arquivo):
	return [tuple([float(num) for num in line.split(';')]) for line in arquivo]

def transf_List(matriz):
	matriz_tmp = list(matriz)
	for i in range(len(matriz)):
		matriz_tmp[i] = list(matriz[i])	
	
	return matriz_tmp

def show_Matriz(matriz):
	for i in range(len(matriz)):
		
		for j in range(len(matriz[0])):
		
			if j == ((len(matriz[0]) - 1)):
				print("%7.3f " %matriz[i][j])
		
			else:
				print("%7.3f " %matriz[i][j], end = " ")

def triang_Matriz(matriz_tmp, vetor_tmp, gauss): #FUNÇÃO PARA TRANSFORMAR A MATRIZ EM TRIANGULAR SUPERIOR
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
		# print("MOD: %d" %mod)		
	if gauss != 1:					
		return matriz_tmp, mod
	else:
		return matriz_tmp, mod, vetor_tmp

def troca_Coluna(matriz, vetor, col):
	for i in range(len(matriz)):
		matriz[i][col] = vetor[0][i]
	
	return matriz

def determ_Matriz(matriz, vetor, det_OG): #FUNÇÃO PARA CALCULAR O DETERMINANTE DA MATRIZ
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

def subs_Retroativa(matriz, vetor, param_A):
	leng = len(matriz)
	res = np.zeros(leng)
	res[leng - 1] = vetor[0][leng - 1] / matriz[leng - 1][leng - 1]
	for i in range(leng - 2, -1, -1):
		soma = 0
		for j in range(i + 1, leng):
			soma = soma + matriz[i][j] * res[j]		
			
		res[i] = round((param_A *((vetor[0][i] - soma)/ matriz[i][i])))	
		if res[i] == -0.0:
			res[i] = 0


	return res

def Cramer(determs, param_A):
	varvs = np.zeros(len(determs) - 1)
	for i in range(len(determs) - 1):
		varvs[i] = param_A * (determs[i + 1]/determs[0])
		if varvs[i] == -0.0:
			varvs[i] = 0

	return varvs

def Gauss(matriz, vetor, param_A):
	vetor_tmp = transf_List(vetor)
	(matriz_tmp, mod, vetor_tmp) = triang_Matriz(transf_List(matriz), vetor_tmp, 1)
	res = subs_Retroativa(matriz_tmp, vetor_tmp, param_A)	

	return res

def Gauss_Jordan(matriz, vetor):
	mod = 0
	matriz_tmp = transf_List(matriz) 
	vetor_tmp = transf_List(vetor)
	res = np.zeros(len(matriz))
	print("\n")
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