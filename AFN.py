class AFN_InicioFim:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3', 'q4'}  # q0: inicial, q4: aceito
        self.estado_inicial = 'q0'
        self.estado_aceitacao = 'q4'

    def transicao(self, estado, caractere_entrada):
        if estado == 'q0':  
            if caractere_entrada == '0':
                return {'q1'}  
        elif estado == 'q1': 
            if caractere_entrada == '1':
                return {'q2'}  
        elif estado == 'q2':  
            if caractere_entrada == '0':
                return {'q2'}  
            elif caractere_entrada == '1':
                return {'q3'}  
        elif estado == 'q3':  
            if caractere_entrada == '1':
                return {'q3'}  
            elif caractere_entrada == '0':
                return {'q4'}
        elif estado == 'q4':
            if caractere_entrada == '1':
                return {'q3'}
            
        return {estado}  

    def aceita(self, string_entrada):
        estados_atuais = {self.estado_inicial}
        for char in string_entrada:
            proximos_estados = set()
            for estado in estados_atuais:
                proximos_estados |= self.transicao(estado, char)
            estados_atuais = proximos_estados
        return self.estado_aceitacao in estados_atuais

# Testando
afn = AFN_InicioFim()
print("0110", afn.aceita("0110"))      # True, começa com "01" e termina com "10"
print("010", afn.aceita("010"))        # False, termina sem "10"
print("110", afn.aceita("110"))        # False, não começa com "01"
print("01010", afn.aceita("01010"))      # True, começa com "01" e termina com "10"
print("0111101", afn.aceita("0111101"))    # False, não termina com "10"
print("0110110", afn.aceita("0110110"))    # True, começa com "01" e termina com "10"
print("01010", afn.aceita("01010"))      # True, começa com "01" e termina com "10"
