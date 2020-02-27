'''Programa que cria um dicionário vazio, então lê o arquivo banco.txt e carrega
os dados do arquivo para o dicionário, para que possam ser utilizados pelo programa.'''
arqbanco = open("banco.txt", "")  # Abre o arquivo banco.txt
banco = {}  # Cria o dicionário banco vazio
# Utilizando o modo R ele lê o arquivo que já foi criado, se não existir dá erro.
for linha in arqbanco.readlines():  # readlines gera uma lista com cada linha.
    linha = linha.split(',')  # Separa cada item da linha com base na virgula
    banco[int(linha[0])] = [str(linha[1]), float(linha[2]), int(linha[3])]
    # Adiciona a linha no banco: 0=Conta, 1=Nome, 2=Saldo, 3=Senha
arqbanco.close()  # Fecha o arquivo
for chave, dados in banco.items():  # Para cada chave e dado nos itens do dicionário Banco
    print("Conta: %d Titular: %s Saldo: %6.2f Senha: %d" % (chave, dados[0], dados[1], dados[2]))
    # Imprime cada linha do dicionário.
