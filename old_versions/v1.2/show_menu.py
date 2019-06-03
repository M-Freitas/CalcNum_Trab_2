import os, platform
from ptables import prettytable

def clear():
	if(platform.system()) == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

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
	dir_dpd_exist = os.getcwd() + '\Termos_dpd.txt'
	dir_idpd_exist = os.getcwd() + '\Termos_idpd.txt'
	
	# print(dir_exist)
	if os.path.exists(dir_dpd_exist) and os.path.exists(dir_idpd_exist):
		print("Arquivos existentes")
	else:
		print("Arquivos Inexistentes")
msg_user()