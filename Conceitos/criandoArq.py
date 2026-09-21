from random import randint

'''O programa a seguir cria um arquivo, chamado "pontos.txt", com 30 pontos bidimensionais (2D), com coordenadas aleatórias (x,y)
no intervalo 0 a 400. Ao final, mostra na tela o conteúdo do arquivo gerado.'''

#Subprogramas
def criaArqPts(nome, qtd, minimo, maximo):
    arq = open(nome, "w")
    for linha in range(qtd):
        arq.write(str(randint(minimo,maximo)) + "," + str(randint(minimo,maximo)) + "\n")
    arq.close()
    return None
    
def mostra(nome):
    arq = open(nome, "r")
    for ponto in arq:
        print(ponto, end="")
    arq.close()
    return None
    
#Programa Principal
criaArqPts("pontos.txt", 30, 0, 400)
mostra("pontos.txt")
