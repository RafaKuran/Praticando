#Conceito básico de listas em compreensão
#Preencher lista apenas com números pares

pares = [x for x in range(20) if x % 2 == 0]
print(pares)