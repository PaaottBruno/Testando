# arm = input(">>> ")
# c = arm.isdigit()
# if c:
#     print("correto")
# if not c:
#     print("erro")

# import getpass
# import os

# import pwinput  # modulo que esconde sua senha com ***, para utilizar deve-se digitar no terminal
#                 # pip install pwinput, e dar um enter pronto estara intalando

# a = pwinput.pwinput("Digite sua senha: ")  # condição para usar o pwinput, deve usar pwinput.pwinput
# print(f"Sua senha digita foi: {a}")

# user = os.getlogin()

# print(f"Meu nome é {user}")

# import getpass

# user = getpass.getpass()

import getpass
  
user = getpass.getuser()

print(f"Meu nome é {user}")

import pwinput

a = pwinput.pwinput("Digite: ")
print(a)
