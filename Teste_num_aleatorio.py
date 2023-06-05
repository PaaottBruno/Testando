from random import randint
import os
dado = {}
cont = 0

while True:
    cont = cont + 1
    
    dado = input("\nd4 = dado de 4 lados\nd6 = dado de 6 lados\
    \nd8 = dado de 8 lados\nd10 = dado de 10 lados\nd12 = dado de 12 lados\
    \nd20 = dado de 20 lados\nd100 = dado de 100 lados\
    \nEscolha o dados desejado: ")
    
    if dado not in 'd4' and dado not in 'd6' and dado not in 'd8' and\
    dado not in 'd10' and dado not in 'd12' and dado not in 'd20' and dado not in 'd100':
        print("\nO dado escolhido não existe\nPor Favor Tente Novamente.\n")
        continue
   
    try:
        quant = int(input("Quantas vezes vc vai rola esse dado: "))
        
    except ValueError:

        print("\nSomente Numeros\n")

    dado = str(dado)
    if dado == 'd4':
        d4 = (randint(1, 4))
        os.system('cls')
        print(4*"=-="+5*" ")
        print(" "*4,quant*d4)
        print(4*"=-="+5*" ")
        dano = quant*d4

    elif dado == 'd6':
        d6 = (randint(1, 6))
        os.system('cls')
        print(4*"=-="+5*" ")
        print(" "*4,quant*d6)
        print(4*"=-="+5*" ")
        dano = quant*d6

    elif dado == 'd8':
        d8 = (randint(1, 8))
        os.system('cls')
        print(4*"=-="+5*" ")
        print(" "*4,quant*d8)
        print(4*"=-="+5*" ")
        dano = quant*d8

    elif dado == 'd10':
        d10 = (randint(1, 10))
        os.system('cls')
        print(" "*4,quant*d10)
        dano = quant*d10

    elif dado == 'd12':
        d12 = (randint(1, 12))
        os.system('cls')
        print(4*"=-="+5*" ")
        print(" "*4,quant*d12)
        print(4*"=-="+5*" ")
        dano = quant*d12

    elif dado == 'd20':
        d20 = (randint(1, 20))
        os.system('cls')
        print(4*"=-="+5*" ")
        print(" "*4,quant*d20)
        print(4*"=-="+5*" ")
        dano = quant*d20

    elif dado == 'd100':
        d100 = (randint(1, 100))
        os.system('cls')
        print(4*"=-="+5*" ")
        print(" "*4,quant*d100)
        print(4*"=-="+5*" ")
        dano = quant*d100
        


    
    # if dado not in 'd4' and dado not in 'd6' and dado not in 'd8' and\
    # dado not in 'd10' and dado not in 'd12' and dado not in 'd20' and dado not in 'd100':
    #     print("\nO dado escolhido não existe\nPor Favor Tente Novamente.\n")
    #     continue

    # # dado = int(dado)

    # if dado >= 0:
    #     print("\nO dado escolhido não existe\nPor Favor Tente Novamente.\n")
    #     continue

    # quant = int(input("Quantas vezes vc vai rola esse dado: "))
    # dado = str(dado)
    # if quant == 0:
    #     print("\nNão e possivel rola '0' vezes o dado\nPor Favor Tente Novamente.\n")
    #     continue

    # if dado == 'd4':
    #     d4 = (randint(1, 4))
    #     os.system('cls')
    #     print(quant*d4,'\n')
    #     dano = quant*d4

    # elif dado == 'd6':
    #     d6 = (randint(1, 6))
    #     os.system('cls')
    #     print(quant*d6,'\n')
    #     dano = quant*d6

    # elif dado == 'd8':
    #     d8 = (randint(1, 8))
    #     os.system('cls')
    #     print(quant*d8,'\n')
    #     dano = quant*d8

    # elif dado == 'd10':
    #     d10 = (randint(1, 10))
    #     os.system('cls')
    #     print(quant*d10,'\n')
    #     dano = quant*d10

    # elif dado == 'd12':
    #     d12 = (randint(1, 12))
    #     os.system('cls')
    #     print(quant*d12,'\n')
    #     dano = quant*d12

    # elif dado == 'd20':
    #     d20 = (randint(1, 20))
    #     os.system('cls')
    #     print(quant*d20,'\n')
    #     dano = quant*d20

    # elif dado == 'd100':
    #     d100 = (randint(1, 100))
    #     os.system('cls')
    #     print(quant*d100,'\n')
    #     dano = quant*d100

    # if dado != 0:        # ajustar bug que possivel usuario pode achar.
    #     print("\nO dado escolhido não existe\nPor Favor Tente Novamente.\n")
    #     continue

print(f"O seu dano foi {dano}")

