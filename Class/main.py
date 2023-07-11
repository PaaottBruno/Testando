import os
class Usuario():

    def __init__(self,nome,idade,cpf,email,endereco):

        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

    def relatorio(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nCPF: {self.cpf}\nEmail:{self.email}\nEndereço: {self.endereco}")
    
    def calculadora(self):
        while True:
            print(8*"=-","Seja Bem vindo a calculadora","=-"*8)
            op = input("1- Mais\n2- Menos\n3- Vezes\n4- Divisão\n5- Raiz Quadrada\nEscreva o nome ou numero da operação que deseja: ")

            op = op.upper()

            if op == "MAIS" or op == "1":
                valor1 = float(input("Digite o primeiro valor: "))
                valor2 = float(input("Digite o segundo valor: "))
                total = valor1 + valor2
                print(f"O valor de {valor1} + {valor2} = {total}")
                os.system("pause")
                os.system("cls")

            elif op == "MENOS" or op == "2":
                valor1 = float(input("Digite o primeiro valor: "))
                valor2 = float(input("Digite o segundo valor: "))
                total = valor1 - valor2
                print(f"O valor de {valor1} - {valor2} = {total}")
                os.system("pause")
                os.system("cls")

            elif op == "VESEZ" or op == "3":
                valor1 = float(input("Digite o primeiro valor: "))
                valor2 = float(input("Digite o segundo valor: "))
                total = valor1 * valor2
                print(f"O valor de {valor1} * {valor2} = {total}")
                os.system("pause")
                os.system("cls")

            elif op == "DIVISAO" or op == "4":
                valor1 = float(input("Digite o primeiro valor: "))
                valor2 = float(input("Digite o segundo valor: "))
                total = valor1 / valor2
                print(f"O valor de {valor1} / {valor2} = {total}")
                os.system("pause")
                os.system("cls")

            elif op == "RAIZ QUADRADA" or op == "5":
                valor1 = float(input("Digite o primeiro valor: "))
                total = valor1 ** (0.5)
                print(total)
                os.system("pause")
                os.system("cls")
                
            else:
                print("*",14*"=-","*")
                print(5*" ","Opção Não Existente"," "*5)
                print("*",14*"=-","*")
    