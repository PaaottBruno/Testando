from random import randint
import os
ladd_ataque =[]
ladd_dano = []
ld4 = []
ld6 = []
ld8 = []
ld10 = []
ld12 = []
ld20 = []
ld100 = []

while True:
    try: 
        
        dado = int(input("\nd4 = dado de 4 lados\nd6 = dado de 6 lados\
        \nd8 = dado de 8 lados\nd10 = dado de 10 lados\nd12 = dado de 12 lados\
        \nd20 = dado de 20 lados\nd100 = dado de 100 lados\
        \nEscolha o dados desejado: d"))   

        if dado != 4 and dado != 6 and dado != 8 and dado != 10 and dado != 12 and dado != 20 and dado != 100:
            print("\nO dado escolhido não existe\nPor Favor Tente Novamente.\n")
            continue
    except:
        os.system('cls')
        print("\nSomente Numeros\n")
        continue
    try:
        quant = int(input("Quantas vezes vc vai rola esse dado: "))
    except ValueError:
        os.system('cls')
        print("\nSomente Numeros\n")
        continue
    try:
            
        if dado == 4:
            d4 = quant*(randint(1, 4))
            ld4.append(d4)
            os.system('cls')
            print(4*"=-="+5*" ")
            print(" "*4,d4)
            print(4*"=-="+5*" ")
            os.system('pause')
            os.system('cls')
            

        elif dado == 6:
            d6 = quant*(randint(1, 6))
            ld6.append(d6)
            os.system('cls')
            print(4*"=-="+5*" ")
            print(" "*4,d6)
            print(4*"=-="+5*" ")
            os.system('pause')
            os.system('cls')
            

        elif dado == 8:
            d8 = quant*(randint(1, 8))
            ld8.append(d8)
            os.system('cls')
            print(4*"=-="+5*" ")
            print(" "*4,d8)
            print(4*"=-="+5*" ")
            os.system('pause')
            os.system('cls')
            

        elif dado == 10:
            d10 = quant*(randint(1, 10))
            ld10a.append(d10)
            os.system('cls')
            print(" "*4,qd10)
            os.system('pause')
            os.system('cls')
            

        elif dado == 12:
            d12 = quant*(randint(1, 12))
            ld12.append(d12)
            os.system('cls')
            print(4*"=-="+5*" ")
            print(" "*4,d12)
            print(4*"=-="+5*" ")
            os.system('pause')
            os.system('cls')
           

        elif dado == 20:
            d20 = quant*(randint(1, 20))
            ld20.append(d20)
            os.system('cls')
            print(4*"=-="+5*" ")
            print(" "*4,d20)
            print(4*"=-="+5*" ")
            os.system('pause')
            os.system('cls')
            

        elif dado == 100:
            d100 = quant*(randint(1, 100))
            ld100.append(d100)
            os.system('cls')
            print(4*"=-="+5*" ")
            print(" "*4,d100)
            print(4*"=-="+5*" ")
            os.system('pause')
            os.system('cls')
              
    except:
        os.system('cls')
        print("\nUsar Somente Numeros\n")
        continue

    add_dano = int(input("Adicionais de dano: "))
    ladd_dano.append(add_dano)

    add_ataque = int(input("Adicionais de ataque: "))
    ladd_ataque.append(add_ataque)

    print(d4+add_dano)