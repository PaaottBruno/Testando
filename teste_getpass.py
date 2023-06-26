import os
from getpass import getpass

def linha():
    print(15*"=-")


lnome = []
lcpf = []
lsexo = []
lsenha = []


cont = 0
while True:
    cont += 1
   
    try:
        menu = int(input("1 - cadastro\n2 - Consulta\n0 - Sair\n>>> "))
    except:
        print("Use apenas numero.")
        break
    os.system('cls')


    if menu == 1:
        linha()
        print(f"O seu cadastro e o {cont}")


        nome = input("Nome: ")
        sexo = input("sexo: ")


        try:
            cpf = int(input("cpf: "))
        except:
            print("Use apenas numeros.")
            continue
        else:
            lnome.append(nome)
            lcpf.append(cpf)
            lsexo.append(sexo)
       

        os.system('cls')
        while True:
            senha = getpass("Senha: ")
            confirm_senha = getpass("Confirmar a senha: ")


            lsenha.append(senha)
            if senha != confirm_senha:
                print("As senhas não são iguais.\nTente Novamente")
                senha = None
                confirm_senha = None

            elif senha == confirm_senha:
                print("Cadastro confirmado com sucesso.")
                os.system('pause')
                break

    elif menu == 2:
        try:
            busca = int(input("busca: "))
        except:
            print("Use apenas numeros.")


        print(lnome[busca-1])
        a = lsenha[busca-1]
        cs = input("Digite a senha: ")
        os.system("pause")


        if cs != a:
            print("Senha incorreta!!")


        elif cs == a:
            print("Senha correta!!")
            print(lnome[busca-1],"\n",lcpf[busca-1],"\n",lsexo[busca-1])
            break


    elif menu == 0:
        print("Programa finalizado.")
        break


