class Pessoa:

    def __init__(self, nome, idade, andando = False):
        self.nome = nome
        self.idade = idade
        self.andando = andando

        
    def andar(self):
        if self.andando:
            print(f"{self.nome} não pode andar pq ja esta andando.")
            return
        print(f"{self.nome} comecou a andar...")
        self.andando = True

    def para(self):
        if not self.andando:
            print(f"{self.nome}parou de andar pq caiu")
            return
        print(f"{self.nome} parou de andar.")
        self.andando = False

a = Pessoa(input("Digite seu nome: "), input("Digite sua idade: "))
a.andar()
a.andar()
a.para()
a.para()
a.andar()