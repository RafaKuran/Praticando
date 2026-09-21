#O self serve para dizer ao Python: "estou mexendo nos dados deste objeto específico que está executando a ação agora". 
#Sem o self., o Python acha que é apenas uma variável temporária local.

class Jogador:
    # O método __init__ é o construtor: ele roda assim que criamos um novo jogador
    def __init__(self, nome, simbolo):
        # Atributos do jogador
        self.nome = nome
        self.simbolo = simbolo
        self.vitorias = 0

    # Método para realizar uma ação
    def ganhar_ponto(self):
        self.vitorias += 1
        print(f"{self.nome} venceu e agora tem {self.vitorias} vitória(s)!")


# --- Criando Objetos (Instâncias da Classe) ---
jogador1 = Jogador("Rafaela", "X")
jogador2 = Jogador("Computador", "O")

# Acessando atributos
print(jogador1.nome)     # Saída: Rafaela
print(jogador2.simbolo)  # Saída: O

# Executando métodos
jogador1.ganhar_ponto()  # Saída: Rafaela venceu e agora tem 1 vitória(s)!