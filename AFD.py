class AFD_BlocosDeZeros:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}  # q0: sem zeros, q1: lendo um zero, q2: após dois zeros consecutivos
        self.estado_inicial = 'q0'
        self.estados_aceitacao = {'q2'}  # Aceita apenas se tiver lido dois zeros consecutivos

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':  
            if caractere_entrada == '0':
                return 'q1'  
            else:
                return 'q0'  
        elif estado == 'q1':  
            if caractere_entrada == '0':
                return 'q2'  
            else:
                return 'q0' 
        elif estado == 'q2':  
            if caractere_entrada == '0':
                return 'q2'  
            else:
                return 'q2' 
        return estado  

    def aceita(self, string_entrada):
        estado_atual = self.estado_inicial
        
        for char in string_entrada:
            estado_atual = self.transicao(estado_atual, char)
        
        return estado_atual in self.estados_aceitacao

# Testando o AFD
afd1 = AFD_BlocosDeZeros()
print("1100", afd1.aceita("1100"))      # True
print("11", afd1.aceita("11"))        # False
print("000", afd1.aceita("000"))       # True
print("1110", afd1.aceita("1110"))       # False
print("10101", afd1.aceita("10101"))    # False
