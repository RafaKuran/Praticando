'''Criando matrizes 2D utilizando compreensão em listas'''
import random

#Como função
def matriz2D(m,n):
    # m -> linhas; n -> colunas
    return [[random.randint(1,10)]*n for _ in range(m)]
    
#print(matriz2D(2,2))

#Parte do código
l = int(input("Quantas linhas: "))
c = int(input("Quantas colunas: "))
n = int(input("Qual o máximo de números a serem escolhidos: "))

a = [[random.randint(1,n) for y in range(c)] for x in range(l)] 

'''
A compreensão acima corresponde as linhas de comando abaixo:

a = []
for x in range(l):
    row = []
    for y in range(c):
        row.append(random.randint(1,10))
    a.append(row)

'''
print(a) #matriz em forma de vetor

#matriz original
for linha in a:
    print(linha, end="")
    print()