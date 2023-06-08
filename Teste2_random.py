from random import randint
cont = 0

quant = int(input("Digite um numero: "))
while True:
    cont += 1
    if quant == cont:
        for i in range(cont):
            print(randint(1, 4))
        
            

    if cont == 5:
        break