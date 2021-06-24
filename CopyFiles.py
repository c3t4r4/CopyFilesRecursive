#!/usr/bin/python3
# coding: utf-8

import subprocess, shlex, os, shutil

pastas = os.listdir()
Destino = os.path.abspath('./') + '/Files/'


total = 0
erro = 0
arq = open("lista_de_arquivos.txt", "w",encoding="utf-8")

def listar_pasta(pasta):
	tot = 0
	subpastas = list()
	if os.path.isdir(pasta):
		items = os.listdir(pasta)
		arq.write("ARQUIVOS NA PASTA '"+ str(pasta).upper() +"': \n")
		for item in items:
			novo_item = os.path.join(pasta,item)
			if os.path.isdir(novo_item) and novo_item != "Files":
				subpastas.append(novo_item)
				continue
			else:
				#print("Novo Item: " + novo_item)
				#print("Item: " + item)
				if(item != ".DS_Store"):
					movefile(novo_item, item)
			

			'''
            verifica = renomeia(novo_item)
            if verifica == 0:
				pass
			else:
				arq.write(verifica + "\n")
				tot += 1
            '''
		for subpasta in subpastas:
			tot += listar_pasta(subpasta)
	arq.write("\n")
	return tot

def movefile(filepath, filename):
	nome = filename
	origem = filepath
	destino = Destino + nome
	print('Arquivo - ' + nome)
	print('Path - ' + origem)
	shutil.copy2(origem, destino)

if __name__ == '__main__':
	os.system('mkdir Files')
	for pasta in pastas:
		total +=  listar_pasta(pasta)
	arq.write("# Total de arquivos : "+ str(total))
	arq.close()
	#os.system('chmod -x *')
	#os.remove('MudarTodosNomes.py')
	if erro == 0:
		#os.system('clear')
		print('Script Finalizado SEM ERROS')
	else:
		print('Script Finalizado COM ERROS')
	print("Total de arquivos: " + str(total))
