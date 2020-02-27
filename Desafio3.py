def verificasenha(c):
    while True:
        s = int(input("Digite sua senha:"))
        if banco[c][2] == s:
            return True
        else:
            print("Senha errada, tente novamente!")


def saldo(c):
    if verificasenha(c):
        print("=" * 1000)
        print("Seu saldo é R$ %8.2f" % banco[c][1])


def saque(c):
    valor = float(input("Digite o valor a ser sacado: "))
    if verificasenha(c):
        if valor <= banco[c][1]:
            banco[c][1] -= valor
            print("=" * 1000)
            print("Você sacou R$ %8.2f" % valor)
        else:
            print("=" * 1000)
            print("Seu saldo não é suficiente!!!")


def deposito(c):
    valor = float(input("Digite o valor a ser depositado: "))
    if verificasenha(c):
        banco[c][1] += valor
        print("=" * 1000)
        print("Você depositou R$%8.2f" % valor)


# Inicio do programa principal
arqbanco = open("banco.txt", "r")  # Abre o arquivo banco.txt
banco = {}  # Cria o dicionário banco vazio
# Utilizando o modo R ele lê o arquivo que já foi criado, se não existir dá erro.
for linha in arqbanco.readlines():  # readlines gera uma lista com cada linha.
    linha = linha.split(',')  # Separa cada item da linha com base na virgula
    banco[int(linha[0])] = [str(linha[1]), float(linha[2]), int(linha[3])]
    # Adiciona a linha no banco: 0=Conta, 1=Nome, 2=Saldo, 3=Senha
arqbanco.close()  # Fecha o arquivo
while True:
    conta = int(input("Digite o número de sua conta: "))
    if conta in banco:
        print("=" * 1000)
        print("Bem vindo(a) %s" % banco[conta][0])
        break
    else:
        print("Conta inexistente, tente novamente!")

while True:
    print("="*1000)
    op = int(input("Escolha uma das opções: \n1-Saldo 2-Saque 3-Depósito 4-Sair: "))
    if op == 1:
        saldo(conta)
    elif op == 2:
        saque(conta)
    elif op == 3:
        deposito(conta)
    elif op == 4:
        print("=" * 1000)
        print("Seção encerrada!")
        print("=" * 1000)
        break
    else:
        print("=" * 1000)
        print("Digite uma opção válida!")
arqbanco = open("banco.txt", "w")  # Usando W cria o arquivo, se já existir reescreve.
for chave, dados in banco.items():  # Para cada chave e dado nos itens do dicionário Banco
    arqbanco.write("%d,%s,%8.2f,%d \n" % (chave, dados[0], dados[1], dados[2]))
    # Escreve no arquivo os dados que foram lidos do dicionario
arqbanco.close()  # Fecha o arquivo
