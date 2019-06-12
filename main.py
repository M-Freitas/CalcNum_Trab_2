###############################################################
#AUTOR: MARCOS VINICIUS FREITAS PINTO
#INSTITUIÇÃO: UNIVERSIDADE FEDERAL DO CEARÁ
#CURSO: ESTATÍSTICA
#CONTATO: marcos.freitasp@alu.ufc.br
###############################################################
#coding:utf-8
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
(leng_m, major) = funcs.quad_Matriz(matriz)
leng_v = (len(vct_idpd[0]) == len(matriz))	

if (leng_v == True) and (leng_m == True):

	determs = round(np.linalg.det(matriz))

	if determs != 0:
		res_Gauss = funcs.Gauss(matriz, vct_idpd)
		res_GaussJordan = funcs.Gauss_Jordan(matriz, vct_idpd)
		(res_D, res_Amp) = funcs.Cramer(res_Gauss, param_A)	
		funcs.write_Matriz(matriz, vct_idpd, res_Gauss, res_GaussJordan, res_D, res_Amp, param_A)
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
	if leng_m == False:
		print("\nMatriz com o número de LINHAS diferente do número de COLUNAS!!!\n\nEntrem com uma MATRIZ QUADRADA!!!!!\n")
	if leng_v == False:
		if(len(vct_idpd[0]) < len(matriz[major])):
			print("\nVetor dos TERMOS INDEPENDENTES está com o número de TERMOS, MENOR que o NÚMERO DE LINHAS DA MATRIZ!!!\n\n")
		else:
			print("\nVetor dos TERMOS INDEPENDENTES está com o número de TERMOS, MAIOR que o NÚMERO DE LINHAS DA MATRIZ!!!\n\n")
	show_menu.enter(2)
	show_menu.clear()
