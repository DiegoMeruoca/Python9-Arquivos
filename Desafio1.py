'''Programa que abre o arquivo numeros.txt e solicita para o usuário digitar qual
linha deseja que seja a primeira e a ultima na impressão.'''
inicio = int(input("Digite o número da linha que deseja que seja a primeira:"))  # Entrada de Dados
fim = int(input("Digite o número da linha que deseja que seja a ultima:"))  # Entrada de Dados
arquivo = open("numeros.txt", "r")  # Abre o arquivo numeros.txt
# Utilizando o modo R ele lê o arquivo que já foi criado, se não existir dá erro.
for linha in arquivo.readlines():  # readlines gera uma lista com cada linha.
    if inicio <= int(linha) <= fim:  # Se o número obtido na linha estiver entre inicio e fim
        print(linha)  # Printa a linha obtida no arquivo
arquivo.close()  # O método close fecha o arquivo
