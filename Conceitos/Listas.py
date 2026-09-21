#Subprogramas

#Preencher uma lista
def preencher(valores):
    for ind in range(len(valores)):
        valores[ind] = int(input("Elemento["+str(ind)+"]="))
    return None

#Buscar um elemento numa lista
def buscaElemento(valores, procurado):
    for num in range(len(valores)):
        if valores[num] == procurado:
            return print("Valor {} encontrado!".format(valores[num]))
    return print("Valor {} não encontrado!".format(procurado))

#Maior e menor valores
def maiorMenor(valores):
    menor = valores[0]
    maior = valores[0]
    for indice in range(1, len(valores)):
        if menor > valores[indice]:
            menor = valores[indice]
        elif maior < valores[indice]:
            maior = valores[indice]
    return print("{} é o menor valor\n{} é o maior valor".format(menor, maior))

#Programa Principal
n = int(input("Quantidade de elementos nessa lista: "))
numeros = [None]*n
preencher(numeros)
dado = int(input("Digite um valor a ser procurado: "))
onde = buscaElemento(numeros, dado)
extremos = maiorMenor(numeros)







print(onde)
