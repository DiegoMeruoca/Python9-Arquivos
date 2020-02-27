arquivo = open("numeros.txt", "r")  # Abre o arquivo numeros.txt
# Utilizando o modo R ele lê o arquivo que já foi criado, se não existir dá erro.
for linha in arquivo.readlines():  # readlines gera uma lista com cada linha.
    print(linha)  # Printa a linha obtida no arquivo
arquivo.close()  # O método close fecha o arquivo

