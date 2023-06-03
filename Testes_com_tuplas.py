cont = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    num = int(input("Digite um numero entre 0 a 15: "))
    if 0 <= num <= 20:
        con = int(input("Digite o numero '0' para continuar ou  '1' para parar: "))
        if con == 0:
            continue
        elif con == 1:
            break
        break
    print("Tente Novamente...")
print(f"O numero que você digitou foi {cont[num]}")

