class Peca:

    def __init__(self, peso = 0,frente = False , tamanho = 1):
        
        self.peso = peso
        self.frente = frente
        self.tamanho = tamanho
    
    def peao(self):
        if self.peao == 1:
            print("pesado")