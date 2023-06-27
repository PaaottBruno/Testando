import os
from getpass import getpass

lnome = []
lcpf = []
lsexo = []
lsenha = []
lcont = []

def linha_cada():
    print(15*"=-")
def linha():
    print(8*"=+=")
def linha2():
    print(10*"--")

def cadastro(cont):
    if cont == 2:
        menu()
    while True:
        lcont.append(cont)

        linha_cada()
        print(f"Numero do cadastro: {lcont[cont-1]}")
        linha_cada()

        nome = input("\nNome: ")
        linha()
        sexo = input("sexo: ")
        linha()
        break
         
    while True:
        try:
            cpf = int(input("cpf: "))
            tcpf = str(cpf)
            arm = len(tcpf)
            if arm < 11 or arm > 11:
                print("O cpf deve conter 11 numeros\nTente novamente")
                continue
        except:
            print("Use apenas numeros.")
            continue
        else:
            lnome.append(nome)
            lcpf.append(cpf)
            lsexo.append(sexo)
        break
    
    os.system('cls')
    while True:
        linha()
        senha = getpass("Senha: ")
        linha()
        confirm_senha = getpass("Confirmar a senha: ")
        linha()

        lsenha.append(senha)
        if senha != confirm_senha:
            print("As senhas não são iguais.\nTente Novamente")
            senha = None
            confirm_senha = None
            del lsenha[cont-1]
            os.system('cls')

        elif senha == confirm_senha:
            linha2()
            print("Cadastro confirmado com sucesso.")
            linha2()
            os.system('pause')
            os.system('cls')
            break
        
def consulta():
    while True:
        try:
            busca = int(input("Digite o numero do cadastro: "))
        except:
            print("Usar apenas numeros.")

        try:

            print(lnome[busca-1],f" Cadastro {busca}")
            a = lsenha[busca-1]
            cs = getpass("Digite a senha: ")
            os.system("pause")

            if cs != a:
                print("Senha incorreta!!\nTente Novamente\n")
                break

            elif cs == a:
                
                print("\nSenha correta!!")
                linha2()
                print("\n",lnome[busca-1],"\n",lcpf[busca-1],"\n",lsexo[busca-1].upper())
                linha2()
                os.system('pause')
                os.system('cls')
                break
        except UnboundLocalError:
            print("\nNão existe nenhum cadastro para consultar.")
            break

        except IndexError:
            print("\nNão existe nenhum cadastro para consultar.")
            break

def menu():
    
    while True:
        
        try:
            print(8*"=-","Seja Bem vindo ao programa getpass()","-="*8,"\n")
            menu = int(input("\n1 - Cadastro\n2 - Consulta\n0 - Sair\n>>> "))
        except:
            print("\nUse apenas numero.\n")
            continue
        
        os.system('cls')

        if menu == 1:
            cont = 0
            while True:
                cont += 1
                cadastro(cont)

        elif menu == 2:
            consulta()

        elif menu == 0:
            print("\nPrograma finalizado.")
            break
    
menu()