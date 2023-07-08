class Animal():

    def __init__(self,nome):

        self.nome = nome

class Cachorro(Animal):

    def __init__(self,nome, correr= False):
        super().__init__(nome)
        self.correr = correr

    def correndo(self):
        print(f"{self.nome} esta correndo")
        self.correr = True

ani = Cachorro("mario")
ani.correndo()



