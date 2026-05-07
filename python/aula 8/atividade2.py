# atividades clan code
# manipulação de arquivos
# import os


# manipulacao_arquivos = "    Manipulação de arquivos e Texto com Python Clean Code    "
# print(manipulacao_arquivos.upper()) # Maiúsculas
# print(manipulacao_arquivos.lower()) # Minúsculas
# print(manipulacao_arquivos.strip()) # Remove espaços em branco
# print(manipulacao_arquivos.split()) # Divide a string em uma lista de palavras
# print(manipulacao_arquivos.replace("Python", "Java")) # Substitui "Python" por "Java"
# print(manipulacao_arquivos.replace(" ", "_")) # Substitui "Espaço" por "_"
# print(manipulacao_arquivos.count("a")) # Conta quantas vezes a letra "a" aparece na string
# print(manipulacao_arquivos.count("Python")) # Conta quantas vezes a palavra "Python" aparece na string
# print(manipulacao_arquivos.upper().count("PYTHON")) # Conta quantas vezes a letra "PYTHON" aparece na string e converte para maiúsculas
# print(manipulacao_arquivos.strip().count("python")) # Conta quantas vezes a letra "python" aparece na string, removendo os espaços em branco
# print(manipulacao_arquivos.find("python")) # retorna a ptimeira posição da palavra indicada "python" na string 
# print(manipulacao_arquivos.title()) #converte a primeira letra de cada palavras para minuscula 
# print(manipulacao_arquivos.swapcase()) # Converte as letras maiúsculas para minúsculas e vice-versa
# print(manipulacao_arquivos.center(50, "*")) #centraliza a string e preenche com "*" ate atingir 50 caracteres
# print(manipulacao_arquivos.startswith("      Manipulaçao")) #verifiva a string começa com "     Manipulaçao "

# # Exercicio 1:
# # Crie um algoritmo onde peça para inserir uma frase e deixa-a formatada com maiuscula e acrescente uma contagem de cada frase.

# frase_usuario = input("Inserir frase :) ")
# print(frase_usuario.upper())
# print(frase_usuario.count(frase_usuario))
# print(frase_usuario.count(""))

# with open ("arquivo.txt", "w") as exemplo:
#     exemplo.write("Exemplo de Clean Code - Aula 8 \n")
#     exemplo.write("Continuando a escrever no arquivo \n")
# # w = write - Escreve no arquivo, se o arquivo já existir, ele irá sobrescrever o conteúdo.

# # Manipulacao de Arquivos
# # Escrevendo em um arquivo
# with open ("arquivo.py" , "w") as python:
#     python.write('print("exemplo python)')



# #lendo o arquivo

# with open ("arquivo.txt", "r") as exemplo:
#     conteudo = exemplo.read()
#     print(conteudo)
# # r = read - Lê o conteúdo do arquivo, se o arquivo não existir, ele irá gerar um erro.

# with open ("arquivo.py","a") as python:
#     python.write('\nprint("Continuando a escrever no arquivo Python")')
#     python.write('\nprint("Mais uma linha no arquivo Python")')
#     python.write('\nprint("Última linha no arquivo Python")')
# # a = append - Adiciona conteúdo ao final do arquivo, se o arquivo não existir, ele irá criar um novo arquivo.
import os
#criando diretorio
# os.mkdir("Teste")

# Renomear pastas
#os.rename("Teste","Aulas")

#excluir pastas 
# os.rmdir("Aulas")

#criar arquivos
# os.mknod("teste.txt")
# os.touch("aula.txt")

# listagem de diretorios 

# print(os.listdir()) #lista os arquivos e pastas dos diretorio atual 
# print(os.listdir("..")) #listas os arquivos e pastas do diretorio pai 
# print(os.listdir("c:\\")) #lista os arquivos e pastas do diretorio raiz do C


#Crie um algoritmo para a criação de um arquivo que irá desligar o computador

# with open("Desligar.bat" , "w") as desligar:
#     desligar.write('shutdown /s /t 300 /c "Sextou! Pode descansar"')

# #Exercicio 3
# with open("Cancelar.bat" , "w") as cancelar:
#     cancelar.write('shutdown /a')

# #Exercicio 4
# #Crie um algoritmo para listar os arquivos do diretório atual e do diretório pai.
# import os
# print("Arquivos do diretório atual: ")
# print(os.listdir())

#Exercicio 5
import os
# os.mkdir("Teste 1")
# os.rename("Teste 1","cebola")
os.rmdir("cebola")
