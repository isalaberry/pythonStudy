#obtendo o diretório atual
import os
cwd=os.getcwd()
print("Diretório atual:",cwd)

#listando arquivos em um diretório
arquivos=os.listdir(cwd)
print("Arquivos no diretório:",arquivos)

#obtendo argumentos da linha de comando
import sys
argumentos=sys.argv
print("Argumentos da linha de comando:",argumentos)

#exemplo prático de navegação por arquivos e diretórios
def listar_arquivos(diretorio):
    try:
        arquivos = os.listdir(diretorio)
        print(f"Arquivos em '{diretorio}':")
        for arquivo in arquivos:
            print(arquivo)
    except FileNotFoundError:
        print(f"Diretório '{diretorio}' não encontrado.")

listar_arquivos(cwd)