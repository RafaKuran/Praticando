#Para que o tabuleiro consiga registrar a marcação de um jogador (X ou O), precisamos de um método que:

# 1º Receba a linha e a coluna escolhidas;

# 2ºVerifique se essa posição está vazia (espaço em branco " ");

# 3ºMarque a posição com o símbolo do jogador se estiver livre, ou avise se a posição já estiver ocupada.

class Tabuleiro:
    def __init__(self):
        #Cria matriz 3x3 com lista em compreensão
        self.matriz = [[" "for _ in range(3)] for _ in range(3)]
    
    def exibir(self):
        for linha in self.matriz:
            print(" | ".join(linha))
            print("-" * 9)

    def fazer_jogada(self, linha, coluna, simbolo):
        # Valida se a posição está dentro dos limites da matriz 3x3
        if 0 <= linha <= 2 and 0 <= coluna <= 2:
            # Verifica se o espaço está vazio
            if self.matriz[linha][coluna] == " ":
                self.matriz[linha][coluna] = simbolo
                return True
            else:
                print("Posição já ocupada! Tente outra.")
                return False
        else:
            print("Posição inválida! Escolha valores entre 0 e 2.")
            return False

    def verificar_vitoria(self, simbolo):
        # 1. Verifica Linhas
        for linha in self.matriz:
            if all(celula == simbolo for celula in linha):
                return True

        # 2. Verifica Colunas
        for col in range(3):
            if all(self.matriz[lin][col] == simbolo for lin in range(3)):
                return True

        # 3. Verifica Diagonais
        if all(self.matriz[i][i] == simbolo for i in range(3)):
            return True
        if all(self.matriz[i][2 - i] == simbolo for i in range(3)):
            return True

        return False

    def esta_cheio(self):
        # Verifica se deu empate (todas as posições preenchidas)
        return all(celula != " " for linha in self.matriz for celula in linha)

    
class Jogador:
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogadores = [
            Jogador("Jogador 1", "X"),
            Jogador("Jogador 2", "O")
        ]
        self.turno = 0

    def iniciar(self):
        print("=== INICIANDO O JOGO DA VELHA OO ===")
        
        while True:
            self.tabuleiro.exibir()
            jogador_atual = self.jogadores[self.turno % 2]
            print(f"\nÉ a vez de {jogador_atual.nome} ({jogador_atual.simbolo})")

            try:
                linha = int(input("Escolha a linha (0-2): "))
                coluna = int(input("Escolha a coluna (0-2): "))
            except ValueError:
                print("⚠️ Por favor, digite apenas números entre 0 e 2!")
                continue

            if self.tabuleiro.fazer_jogada(linha, coluna, jogador_atual.simbolo):
                if self.tabuleiro.verificar_vitoria(jogador_atual.simbolo):
                    self.tabuleiro.exibir()
                    print(f"\n🎉 Parabéns! {jogador_atual.nome} venceu!")
                    break
                
                if self.tabuleiro.esta_cheio():
                    self.tabuleiro.exibir()
                    print("\n🤝 Deu Empate!")
                    break

                # Alterna o turno
                self.turno += 1


# --- Para rodar o jogo ---
if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.iniciar()

