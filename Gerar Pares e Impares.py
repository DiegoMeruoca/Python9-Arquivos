'''Programa que cria o arquivo impares.txt e pares.txt e armazena neles respectivamente
os números impares e pares de 0 a 99'''
impares = open("impares.txt", "w")  # Usando W cria o arquivo, se já existir reescreve.
pares = open("pares.txt", "w")  # Usando W cria o arquivo, se já existir reescreve.
for n in range(0, 100):  # Para cada linha no intervalo de 0 até 100
    if n % 2 == 0:  # Se o resto da divisão inteira for igual 0
        pares.write("%d\n" % n)  # Escreve o número no arquivo pares
    else:  # Senão
        impares.write("%d\n" % n)  # Escreve o número no arquivo impares
impares.close()  # Fecha o arquivo impares
pares.close()  # Fecha o arquivo pares
