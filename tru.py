'''num = float(input("Digite um numero: "))
raiz = num**(1/3)
print(f"A raiz de {num} é {raiz}",end=" ")
print("numero inteiro dele é %.0f"%raiz) 
'''
soma = []
while True:
    
    num1  = float(input("Digite um numero: "))
    num2  = float(input("Digite um numero: "))
    num3  = float(input("Digite um numero: "))
    soma1 = (num1+num2+num3)
    soma.append(soma1)
    a = max(soma)
    print(a)