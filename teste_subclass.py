# class Animal():
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def func(self):
#         print(f"{self.nome} tem {self.idade}")


# class Cachorro(Animal):

#     def __init__(self, nome, idade):
#         super().__init__(nome, idade)

#         self.raca = raca
#         self.tamanho = tamanho

#     def info(self):
#         print(f"{self.nome} tem a idade {self.idade} da raça {self.raca} com o tamanho {self.tamanho}")

# ani = Cachorro("Tijolinho",10,"Pitbul","0.45")
# ani.info()
# ani.func()

class As():

    def __init__(self, nome):
        self.nome = nome

op = input("Nome: ")
p1 = As(op)
print(p1.nome)
p1.As()