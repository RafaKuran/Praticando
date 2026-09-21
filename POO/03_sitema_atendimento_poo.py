#Simular um sistema de atendimento médico
#Teremos:
# 1º Pessoas e Papéis:
# Paciente: Nome, CPF, sintomas, status de atendimento.
# Medico: Nome, CRM, especialidade, status (disponível ou ocupado).
# Enfermeiro: Nome, COREN, responsável por realizar a triagem.

# 2º Fluxo do Sistema:
# O Enfermeiro faz a triagem do Paciente (define a prioridade/sintoma).
# O Medico atende o Paciente da fila.

class Paciente:
    def __init__(self, nome, cpf, sintomas):
        self.nome = nome
        self.cpf = cpf
        self.sintomas = sintomas
        self.prioridade = "Normal"  # Pode mudar na triagem para "Alta" ou "Baixa"
        self.atendido = False

    def __repr__(self):
        return f"Paciente({self.nome} - Prioridade: {self.prioridade})"


class Medico:
    def __init__(self, nome, crm, especialidade):
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade
        self.disponivel = True

    def atender_paciente(self, paciente):
        if not self.disponivel:
            print(f"Dr(a). {self.nome} já está em atendimento!")
            return False

        self.disponivel = False
        paciente.atendido = True
        print(f"🩺 Dr(a). {self.nome} ({self.especialidade}) está atendendo o paciente {paciente.nome}...")
        return True

    def finalizar_atendimento(self):
        self.disponivel = True
        print(f"✅ Dr(a). {self.nome} finalizou o atendimento e está disponível novamente.")

class Enfermeiro:
    def __init__(self, nome, coren):
        self.nome = nome
        self.coren = coren

    def realizar_triagem(self, paciente, nivel_prioridade):
        # Define a prioridade do paciente
        paciente.prioridade = nivel_prioridade
        print(f"📋 Enfermeiro(a) {self.nome} realizou a triagem de {paciente.nome}. Prioridade definida: {paciente.prioridade}")

class FilaAtendimento:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)
        print(f"📥 {paciente.nome} entrou na fila de espera.")

    def chamar_proximo(self):
        if not self.pacientes:
            print("⚠️ Fila de espera vazia!")
            return None

        # Ordenação simples por prioridade (Alta vem primeiro)
        # Usamos uma regra de ordenação: Alta = 1, Média/Normal = 2, Baixa = 3
        ordem_prioridade = {"Alta": 1, "Normal": 2, "Baixa": 3}
        self.pacientes.sort(key=lambda p: ordem_prioridade.get(p.prioridade, 2))

        # Remove e retorna o primeiro da fila (menor valor de prioridade)
        proximo = self.pacientes.pop(0)
        return proximo

    def exibir_fila(self):
        print("\n--- FILA DE ESPERA ATUAL ---")
        if not self.pacientes:
            print("(Fila vazia)")
        else:
            for i, p in enumerate(self.pacientes, 1):
                print(f"{i}. {p.nome} - Prioridade: {p.prioridade}")
        print("----------------------------\n")


# --- Teste Inicial ---
'''p1 = Paciente("Carlos Silva", "123.456.789-00", "Febre e dor de cabeça")
m1 = Medico("Dra. Ana Santos", "CRM-12345", "Clinica Geral")

print(f"Paciente criado: {p1.nome} - Sintomas: {p1.sintomas}")
print(f"Médico disponível? {m1.disponivel}")

# Realizando um atendimento
m1.atender_paciente(p1)
print(f"Paciente foi atendido? {p1.atendido}")

m1.finalizar_atendimento()
print(f"Médico disponível de novo? {m1.disponivel}")'''

# --- Criando o ambiente do hospital ---
fila = FilaAtendimento()

# Profissionais
enfermeiro = Enfermeiro("Juliana", "COREN-98765")
medico = Medico("Ana Santos", "CRM-12345", "Clínica Geral")

# Pacientes chegando
p1 = Paciente("Carlos Silva", "111.111.111-11", "Dor de cabeça leve")
p2 = Paciente("Maria Oliveira", "222.222.222-22", "Falta de ar forte")
p3 = Paciente("João Souza", "333.333.333-33", "Apenas renovar receita")

# 1. Triagem feita pelo enfermeiro
enfermeiro.realizar_triagem(p1, "Baixa")
enfermeiro.realizar_triagem(p2, "Alta")
enfermeiro.realizar_triagem(p3, "Normal")

# 2. Adicionando os pacientes na fila
fila.adicionar_paciente(p1)
fila.adicionar_paciente(p2)
fila.adicionar_paciente(p3)

# 3. Exibindo a fila organizada
fila.exibir_fila()

# 4. Médico chama o próximo (deve chamar a Maria primeiro por conta da prioridade Alta!)
paciente_chamado = fila.chamar_proximo()
if paciente_chamado:
    medico.atender_paciente(paciente_chamado)

# 5. Exibindo a fila após a chamada
fila.exibir_fila()