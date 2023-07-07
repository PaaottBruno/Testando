from teste_subclass import *

class Cachorro(Animal):

    def __init__(self, nome, idade, raca, tamanho):
        super().__init__(nome, idade)

        self.raca = raca
        self.tamanho = tamanho

    def info(self):
        print(f"{self.nome} tem a idade {self.idade} da raça {self.raca} com o tamanho {self.tamanho}")

ani = Cachorro(nome,idade"Pitbul","0.45")
ani.info()