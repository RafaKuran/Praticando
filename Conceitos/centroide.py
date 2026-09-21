'''O programa a seguir é um complemento do exercício CriandoArq, e faz a leitura do arquivo "pontos.txt", com
pontos 2D, com coordenadas (x,y). Calcula e escreve o centroide de todos os pontos lidos.'''

#Subprograma
def centroide(nome):
  arquivo = open(nome, "r")
  qtdPontos = 0
  somaX = 0
  somaY = 0
  for coordenada in arquivo:
    partes = coordenada.split()
    somaX += float(partes[0])
    somaY += float(partes[1])
    qtdPontos += 1
    if qtdPontos == 0:
      print(arquivo.name, "-vazio!!!")
    else:
      print("Ponto calculado: (", somaX/qtdPontos, ",", somaY/qtdPontos, ")." )
    return None
  
#Programa Principal
centroide("pontos.txt")
