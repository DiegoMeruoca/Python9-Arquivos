arquivo = open("numeros.txt", "w")  # Abre o arquivo numeros.txt
# Utilizando o modo W ele cria o arquivo se não existir, caso contrário reescreve.
for linha in range(1,101):  # Para cada linha no intervalo de 1 até 101
    arquivo.write("%d\n" % linha)  # O método write permite "escrever" no arquivo
arquivo.close()  # O método close fecha o arquivo
'''Obs: Quando executarmos o programa não aparecerá nada na tela, mas será gerado
   o arquivo numeros.txt dentro da pasta do projeto onde salvamos este código,
   e este arquivo estará com a lista que criamos no for.
   Caso você altere o arquivo através do bloco de notas, ao executar o programa 
   novamente ele será reescrito, pois utilizamos o modo W'''
