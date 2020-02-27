'''Programa que lê os arquivo pares.txt e impares.txt e gera um novo arquivo chamado
'Par e Impar.txt', com todas as linhas dos outros dois arquivos, de forma a preservar
a ordem numérica.'''
arqpares = open("pares.txt", "r")  # Abre o arquivo pares.txt
arqimpares = open("impares.txt", "r")  # Abre o arquivo impares.txt
# Utilizando o modo R ele lê o arquivo que já foi criado, se não existir dá erro.
listpares = []  # Cria a lista listpares vazia
listimpares = []  # Cria a lista listimpares vazia
for linha in arqpares.readlines():  # readlines gera uma lista com cada linha.
    listpares.append(int(linha))  # Adiciona o dado do arquivo na lista
for linha in arqimpares.readlines():  # readlines gera uma lista com cada linha.
    listimpares.append(int(linha))  # Adiciona o dado do arquivo na lista
arqpares.close()  # O método close fecha o arquivo
arqimpares.close()  # O método close fecha o arquivo
parimpar = open("par e impar.txt", "w")  # Usando W cria o arquivo, se já existir reescreve.
cont = 0  # cria uma variavel para contagem iniciando em 0
while cont < len(listpares):  # Enquanto cont for menor que o comprimento da lista pares
    parimpar.write("%d\n" % listpares[cont])
    # Escreve no arquivo o item da listpares na posição cont
    parimpar.write("%d\n" % listimpares[cont])
    # Escreve no arquivo o item da listimpares na posição cont
    cont += 1  # Acrecenta um a variavel cont
parimpar.close()  # Fecha o arquivo
