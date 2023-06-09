from datetime import date

def voto(a=0):
    atual = date.today().year
    s = atual-a
    print(s)
    return s


ano = int(input("Digite o ano em que nasceu: "))

if voto(ano) >= 16 and voto(ano) <= 18:
    print("Opcional")

elif voto(ano) >= 18:
    print("Obrigatorio")

elif voto(ano) <=15:
    print("Negado")