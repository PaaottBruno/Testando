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

def cadastro(cont):    #   função cadastro, faz o cadastro de uma pessoa.
    if cont == 2:
        menu()

    while True:
        lcont.append(cont)
        
        linha_cada()
        print(f"Numero do cadastro: {sum(lcont)}")      # Informa qual o numero do cadastro ao usuario
        linha_cada()

        nome = input("Nome: ")      
        linha()
        sexo = input("sexo: ")
        linha()
        break
         
    while True:
        try:
            cpf = input("cpf: ")
            arm = len(cpf)
            if arm != 11:   # identifica se o cpf do usuario tem 11 digitos.
                print("O cpf deve conter 11 numeros\nTente novamente")  # informa que o cpf n tem os 11 digitos necessarios
                continue
        except:
            print("Use apenas numeros.")
            continue
        else:
            lnome.append(nome)  
            lcpf.append(cpf)        # armmazena em uma lista os dados do usuario
            lsexo.append(sexo)
        break
    
    os.system('cls')
    while True:
        linha()
        senha = getpass("Senha: ")      # getpass oculta a 'senha' que o usuario escreve
        linha()
        confirm_senha = getpass("Confirmar a senha: ")
        linha()

        lsenha.append(senha)
        if senha != confirm_senha:      # confirma se a senha digita esta igual a senha de confirmação
            print("As senhas não são iguais.\nTente Novamente")
            senha = None
            confirm_senha = None
            del lsenha[cont-1]      # deleta a senha que a pessoa inserio errado
            os.system('cls')

        elif senha == confirm_senha:     # identifica que a senha igual a confirmação da senha
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
            os.system('pause')
            os.system('cls')
            continue
        try:

            print(lnome[busca-1],f"| Cadastro {busca}")
            a = lsenha[busca-1]
            cs = getpass("Digite a senha: ")
            os.system("pause")

            if cs != a:
                os.system('cls')
                print("\nSenha incorreta!!\nTente Novamente\n")
                os.system('pause')
                os.system('cls')
                break

            elif cs == a:
                
                print("\nSenha correta!!")
                linha2()
                print("\nNome: ",lnome[busca-1],"\nCPF: ",lcpf[busca-1],"\nSexo: ",lsexo[busca-1].upper(),"\n")
                linha2()
                os.system('pause')
                os.system('cls')
                break
        except UnboundLocalError:
            print("\nNão existe nenhum cadastro para consultar.")
            os.system('pause')
            os.system('cls')
            break

        except IndexError:
            print("\nNão existe nenhum cadastro para consultar.")
            os.system('pause')
            os.system('cls')
            break

def menu():
    while True:
        
        try:
            print("\n\n",8*"=-","Seja Bem vindo ao programa getpass()","-="*8,"\n")
            menu = int(input("\n1 - Cadastro\n2 - Consulta\n0 - Sair\n>>> "))

            os.system('cls')
        except:
            print("\nUse apenas numero.\n")
            os.system('pause')
            os.system('cls')
            continue
        else:
            if menu == 1:
                cont = 0
                while True:
                    cont += 1
                    cadastro(cont)
                    break

            elif menu == 2:
                consulta()
            
            elif menu == 0:
                print("\nPrograma finalizado.")
                break
            else:
                os.system('cls')
                print("Numero invalido!!!\nTente novamente")
                os.system('pause')
                os.system('cls')
            
menu()