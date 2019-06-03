import os, platform
from ptables import prettytable

def clear():
	if(platform.system()) == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

def enter(opc):
	if opc == 1:
		input("\nPressione a tecla ENTER para prosseguir, caso tenha certeza que os arquivos\nestão criados.")
	if opc == 2:
		input("\nPressione a tecla ENTER para terminar o programa")
def loop_arq(dir_dpd, dir_idpd):
	while (os.path.exists(dir_dpd) and os.path.exists(dir_idpd)) != True:
		input("\nARQUIVOS INEXISTENTES!!\nPressione a tecla ENTER para que sejam criados!!\n")
		arq_dpd = open('Termos_dpd.txt', 'a')
		arq_dpd.close()
		arq_idpd = open('Termos_idpd.txt', 'a')	
		arq_idpd.close()
	return 0

def msg_user():
	table_show = prettytable.PrettyTable()
	table_show.title = "---------- Elimanação por Gauss e Gauss-Jordan ----------"
	table_show.field_names = ["Serão necessários os seguintes arquivos no --> MESMO <-- diretório"]
	table_show.align["Serão necessários os seguintes arquivos no --> MESMO <-- diretório"] = 'l'
	table_show.add_row([""])
	table_show.add_row(["Será preciso um arquivo chamado 'termos_dpd.txt' com os valores dos termos\ndependentes, sendo os valores separados por ';'.\nPor exemplo:"])
	table_show.add_row(["\n10;1;1\n1;10;1\n1;1;10\n"])
	table_show.add_row(["Também será necessário um arquivo chamado 'termos_idpd.txt' com os valores\ndos termos independentes, sendo os valores separados por ';'.\nPor exemplo:\n"])
	table_show.add_row(["12;12;12"])
	clear()
	print(table_show)
	dir_dpd = os.getcwd() + '\Termos_dpd.txt'
	dir_idpd = os.getcwd() + '\Termos_idpd.txt'
	
	enter(1)
	if (os.path.exists(dir_dpd) and os.path.exists(dir_idpd)) == False:
		loop_arq(dir_dpd, dir_idpd)
		clear()	
		print("\nENTRE COM OS VALORES NOS RESPECTIVOS ARQUIVOS E VOLTE A EXECUTAR O PROGRAMA!!\n")
		enter(2)
		clear()
		exit(0)