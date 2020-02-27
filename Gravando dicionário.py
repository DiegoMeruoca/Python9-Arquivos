'''Programa que cria um dicionário, então cria o arquivo notas.txt e escreve
os dados no arquivo, para que possam ser mantidos mesmo após encerrar o programa.'''
notas = {"Peter Oliveira Parker": [5.5, 8, 6],
         "Barry Francisco Allen": [7.5, 4.3, 6],
         "Oliver da Silva Queen": [3.5, 5, 6],
         "Bruce dos Santos Wayne": [10, 10, 10],
         "Tony Aparecido Stark": [10, 10, 10]}  # Gera o dicionario notas
arqnotas = open("notas.txt", "w")  # Usando W cria o arquivo, se já existir reescreve.
for chave, dados in notas.items():  # Para cada chave e dado nos itens do dicionário Banco
    arqnotas.write("%s,%6.2f,%6.2f,%6.2f \n" % (chave, dados[0], dados[1], dados[2]))
    # Escreve no arquivo os dados que foram lidos do dicionario
arqnotas.close()  # Fecha o arquivo
