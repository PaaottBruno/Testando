arm = input(">>> ")
c = arm.isdigit()
if c:
    print("correto")
if not c:
    print("erro")

import getpass

nome = input("Digite seu nome: ")
user = getpass.getuser()

print(f"Meu nome é {user}")

import pynput

a = pynput("Digite: ")