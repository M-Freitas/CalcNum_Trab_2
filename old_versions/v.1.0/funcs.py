import random as rd
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

def triang_Matriz(matriz_tmp): #FUNÇÃO PARA TRANSFORMAR A MATRIZ EM TRIANGULAR SUPERIOR
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
	
	return matriz_tmp, mod

def troca_Coluna(matriz, vetor, col):
	for i in range(len(matriz)):
		matriz[i][col] = vetor[0][i]
	
	return matriz

def determ_Matriz(matriz, vetor, det_OG): #FUNÇÃO PARA CALCULAR O DETERMINANTE DA MATRIZ
	determs = np.ones(len(matriz) + 1)

	if det_OG:
		(matriz_tmp, mod) = triang_Matriz(transf_List(matriz))
		for i in range(len(matriz_tmp)):
			determs[0] *= matriz_tmp[i][i]
		
		if determs[0] != 0: 
			det_OG = False

	if det_OG == False:
		
		for i in range(len(matriz)):	
			(matriz_tmp, mod) = triang_Matriz(troca_Coluna(transf_List(matriz), vetor, i))
			
			for j in range(len(matriz_tmp)):
				determs[(i + 1)] *= matriz_tmp[j][j]
	
	for i in range(len(determs)):
		if determs[i] == -0.0:
			determs[i] = 0

		elif (mod % 2) != 0:
			determs[i] = -1 * determs[i]
	
	return determs

def Cramer(determs):
	varvs = np.zeros(len(determs) - 1)
	for i in range(len(determs) - 1):
		varvs[i] = determs[i + 1]/determs[0]

	return varvs 