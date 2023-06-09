def somar(a,b,c=0):
    s = a + b + c
    print(f"A soma de {a} + {b} + {c} = {s}")  


op = int(input("DN: "))

num = 2
num1 = 3
if op == 1:
    somar(3,2,5)
elif op == 2:
    somar(num,num1)
elif op == 3:
    somar(int(input("Digite um numero: "))\
,int(input("Digite outro numero: ")),\
int(input("Digite o ultimo numero: ")))
