import random

#Preenchendo uma lista de forma aleatória com o número de elementos dado pelo usuário
def preencher(tamLista):
    lista = []
    for i in range(tamLista):
        lista.append(random.randint(1,20))
    return lista

def sorteio(elementos):
    return random.choice(elementos)
    
num = int(input("Quantos elementos terá sua lista?"))
listaCriada = preencher(num)
numSorteado = sorteio(listaCriada)

print("A lista criada é {} \nO número sorteado foi {}".format(sorted(listaCriada),numSorteado))
