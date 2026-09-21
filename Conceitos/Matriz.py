'''Célula de maior valor em uma matriz, passo-a-passo'''

matriz = []
maximo = 0 #valor máximo
posicao = (0, 0) #posição do maior valor

#Definir quantas linhas e colunas terá essa matriz
lin = int(input("Linhas: "))
col = int(input("Colunas: "))

#Preencher essa matriz de forma interativa
for i in range(lin):
    linha = []
    for j in range(col):
        valor = int(input("Valor a ser inserido em ({}, {}):".format(i,j)))
#As células serão preenchidas pelo usuário, e sua posição será informada
        
        #Verificar se o valor é maior que o atual
        if valor > maximo:
            maximo = valor
            posicao = (i, j)
        
        linha.append(valor) #adiciona valores à linha
        matriz.append(linha) #adiciona a linha à matriz

print("O maior valor está na posição {} e vale {}".format(posicao, maximo))
