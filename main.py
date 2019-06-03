#coding: utf-8
import numpy as np
import funcs, show_menu

show_menu.clear()
show_menu.msg_user()
show_menu.clear()

arq_dpd = open('Termos_dpd.txt', 'r')
arq_idpd = open('Termos_idpd.txt', 'r')
matriz = tuple(funcs.read_Matriz(arq_dpd.readlines()))
vct_idpd = funcs.read_Matriz(arq_idpd.readlines())

param_A = funcs.dif_Zero('parâmetro A')
	

if len(matriz) == len(matriz[0]):

	determs = funcs.determ_Matriz(matriz, vct_idpd, True)

	if determs[0] != 0:
		res_Cramer = funcs.Cramer(determs)
		res_Gauss = funcs.Gauss(matriz, vct_idpd)
		res_gauss_jordan = funcs.Gauss_Jordan(matriz, vct_idpd)
		res_final = funcs.res_Final(res_Cramer, res_Gauss, res_gauss_jordan, param_A)	
		funcs.write_Matriz(matriz, vct_idpd, res_Cramer, res_Gauss, res_gauss_jordan, res_final, determs, param_A)
		show_menu.clear()
		print("\nPrograma executado com sucesso!!!\n\nResultados armazenados no arquivo 'res_Sistema.txt'!!\n")
		show_menu.enter(2)
		show_menu.clear()
		exit(0)
	else:
		show_menu.clear()
		print("\nDeterminate da Matriz igual a ZERO!!\n")
		show_menu.enter(2)
		show_menu.clear()
		exit(0)
else:
	show_menu.clear()
	print("\nMatriz com o número de LINHAS diferente do número de COLUNAS!!!\n\nEntrem com uma MATRIZ QUADRADA!!!!!\n")
	show_menu.enter(2)
	show_menu.clear()