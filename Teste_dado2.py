from random import randint
import os
ld4 = []
ld6 = []
ld8 = []
ld10 = []
ld12 = []
ld20 = []
ld100 = []
def linha():
    print(8*"-=")

def dados():
    try:
        try:

            dado = int(input("d4 - dados de 4 lados\nd6 - dados de 6 lados\nd8 - dado de 8 lados\
            \nd10 - dado de 10 lados\nd12 - dados de 12 lados\nd20 - dado de 20 lados\nd100 - dado de 100 lados\
            \nEscolha qual dado deseja rolar\n>>> d"))
        except:
            linha()
            print("Usar Apenas Numeros")
            linha()
        try:
            quant = int(input("Digite a quantidade que deseja rolar o dado: "))
        except:
            linha()
            print("Usar Apenas Numeros")
            linha()
    except:
        linha()
        print("Usar Apenas Numeros")
        linha()
    else:
        try:
            if dado == 4:
                for num in range(quant):
                    d4 = randint(1, 4)
                    tu = ld4.append(d4)
                tu = tuple(ld4)
                os.system('cls')
                print(f"\nO dado escolhido é d{dado}, rolado {quant} vezes\n{tu} o total é {sum(ld4)}\n")
                
            if dado == 6:
                for num in range(quant):
                    d6 = randint(1, 6)
                    tu = ld6.append(d6)
                tu = tuple(ld6)
                os.system('cls')
                print(f"\nO dado escolhido é d{dado}, rolado {quant} vezes\n{tu} o total é {sum(ld6)}\n")

            if dado == 8:
                for num in range(quant):
                    d8 = randint(1, 8)
                    tu = ld8.append(d8)
                tu = tuple(ld8)
                os.system('cls')
                print(f"\nO dado escolhido é d{dado}, rolado {quant} vezes\n{tu} o total é {sum(ld8)}\n")

            if dado == 10:
                for num in range(quant):
                    d10 = randint(1, 10)
                    tu = ld10.append(d10)
                tu = tuple(ld10)
                os.system('cls')
                print(f"\nO dado escolhido é d{dado}, rolado {quant} vezes\n{tu} o total é {sum(ld10)}\n")

            if dado == 12:
                for num in range(quant):
                    d12 = randint(1, 12)
                    tu = ld12.append(d12)
                tu = tuple(ld12)
                os.system('cls')
                print(f"\nO dado escolhido é d{dado}, rolado {quant} vezes\n{tu} o total é {sum(ld12)}\n")

            if dado == 20:
                for num in range(quant):
                    d20 = randint(1, 20)
                    tu = ld20.append(d20)
                tu = tuple(ld20)
                os.system('cls')
                print(f"\nO dado escolhido é d{dado}, rolado {quant} vezes\n{tu} o total é {sum(ld20)}\n")

            if dado == 100:
                for num in range(quant):
                    d100 = randint(1, 100)
                    tu = ld100.append(d100)
                tu = tuple(ld100)
                os.system('cls')
                print(f"\nO dado escolhido é d{dado}, rolado {quant} vezes\n{tu} o total é {sum(ld100)}\n")
        except:
            print()           
    finally:
        print()


def main():
    
    op = input("Digite\n1 - dados\n2 - 'Inexistente'\nsair\n>>> ")
    if op == 'sair':
        print()
    switcher = {
        "1": dados,
    }

    acao = switcher.get(op)
    if acao:
        acao()
    else:
        print("Tente Novamente")

main()