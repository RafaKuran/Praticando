class Calculadora:
    def __init__(self):
        pass
    
    def somar(self,a,b):
        return a+b
    
    def multiplicar(self,a,b):
        return a * b

calculadora = Calculadora()

soma = calculadora.somar(3,7)
produto = calculadora.multiplicar(7,8)

print("A soma é igual a",soma," e o produto é igual a", produto)