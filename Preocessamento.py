largura = 100
entrada = open("entrada.txt")  # Abre o arquivo entrada.txt
# não informando o modo, ele automaticamente abre como R, apenas leitura.
for linha in entrada.readlines():  # readlines gera uma lista com cada linha.
    if linha[0] == ";":  # Se o primeiro elemento da linha for igual ;
        continue  # o programa continua
    elif linha[0] == ">":  # Se o primeiro elemento da linha for igual >
        print(linha[1:].rjust(largura))  # Alinha a direita de acordo com a Largura
    elif linha[0] == "<":  # Se o primeiro elemento da linha for igual <
            print(linha[1:].ljust(largura))  # Alinha a esquerda de acordo com a Largura
    elif linha[0] == "*":  # Se o primeiro elemento da linha for igual *
        print(linha[1:].center(largura))  # Alinha ao centro de acordo com a Largura
    else:  # Senão
        print(linha)  # Imprime normal
entrada.close()  # Fecha o arquivo
