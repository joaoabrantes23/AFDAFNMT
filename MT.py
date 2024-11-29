class MaquinaDeTuring:
    def __init__(self):
        # Estados da máquina
        self.estados = {'q0', 'q1', 'q2', 'q_aceita', 'q_rejeita'}
        self.estado_inicial = 'q0'
        self.estado_aceitacao = 'q_aceita'
        self.estado_rejeicao = 'q_rejeita'
        # Transições
        self.transicoes = {
            # Estado q0: Processa o primeiro caractere
            ('q0', 'a'): ('q1', 'x', 'D'),  
            ('q0', 'b'): ('q2', 'x', 'D'), 
            ('q0', '_'): ('q_aceita', '_', 'N'),  # Fita vazia ou palíndromo de comprimento ímpar

            # Estado q1: Avança para o próximo caractere
            ('q1', 'a'): ('q1', 'a', 'D'),  
            ('q1', 'b'): ('q1', 'b', 'D'),  
            ('q1', 'x'): ('q1', 'x', 'D'),  
            ('q1', '_'): ('q2', '_', 'E'),  # Começa a voltar para comparar os caracteres

            # Estado q2: Processa o segundo caractere e volta para o início
            ('q2', 'a'): ('q2', 'a', 'E'), 
            ('q2', 'b'): ('q2', 'b', 'E'),  
            ('q2', 'x'): ('q0', 'x', 'D'),  # Voltando para q0 para verificar o próximo par
            ('q2', '_'): ('q_rejeita', '_', 'N'),  # Não tem mais caracteres a comparar
        }

    def executar(self, fita):
        fita = list(fita) + ['_']  # Adiciona espaço vazio no final
        posicao = 0  # Cabeça começa no início da fita
        estado_atual = self.estado_inicial

        while estado_atual not in {self.estado_aceitacao, self.estado_rejeicao}:
            simbolo_atual = fita[posicao]
            chave_transicao = (estado_atual, simbolo_atual)

            if chave_transicao not in self.transicoes:
                estado_atual = self.estado_rejeicao
                break

            # Nova configuração
            novo_estado, novo_simbolo, movimento = self.transicoes[chave_transicao]
            fita[posicao] = novo_simbolo
            estado_atual = novo_estado

            # Movimento da cabeça
            if movimento == 'D':  # Direita
                posicao += 1
            elif movimento == 'E':  # Esquerda
                posicao -= 1

            # Ajusta os limites da fita
            if posicao < 0:
                fita.insert(0, '_')
                posicao = 0
            elif posicao >= len(fita):
                fita.append('_')

        return estado_atual == self.estado_aceitacao


# Testando a Máquina de Turing
mt = MaquinaDeTuring()

# Casos de teste
testes = [
    "aaaa",  # Aceita (apenas 'a's)
    "aaab",  # Rejeita (contém 'b')
    "a",     # Aceita (apenas 'a')
    "bb",     # Rejeita (apenas 'b')
    "aaaaa", # Aceita (apenas 'a's)
    "",      # Aceita (fita vazia)
]

print("Resultados dos Testes:")
for teste in testes:
    resultado = mt.executar(teste)
    print(f"Entrada: '{teste}' -> {'Aceita' if resultado else 'Rejeitada'}")
