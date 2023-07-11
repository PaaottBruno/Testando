from main import*
import os

while True:
    opcao = input("1 - Cadastro\n2 - Relatorio do cadastro\n3 - Calculadora\n4 - Lanchonete\n>>> ")

    print(8*"=-","Digite seus dados","=-"*8)

    nome = input("Nome: ")
    try:

        idade = int(input("Idade: "))
        cpf = int(input("CPF: "))

    except ValueError:
        print("Use apenas numeros")
        os.system("pause")
        os.system("cls")
        continue

    email = input("Email: ")
    endereco = input("Enderço: ")

    u1 = Usuario(nome,idade,cpf,email,endereco)

    print(8*"=-","Cadastro Concluido","=-"*8)

    if opcao == 
    elif opcao == "2":
        os.system("cls")
        u1.relatorio()
    elif opcao == "3":
        os.system("cls")
        u1.calculadora()
    elif opcao == "4":
        os.system("cls")
        u1.lanchonete()
    else:
        print("Opção não existente!!!")