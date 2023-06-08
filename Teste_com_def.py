c = '♘'
t ='♖'
b = '♗'
ra = '♕'
re = '♔'
p = '♙'
linhaL = "|    |    |    |    |    |    |    |    |"
linhaT = "-------------------------------------------"
def tabuleiro():
    print("   | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  |")
    print(linhaT)
    print(f"A  | {t}  | {c}  | {b}  | {ra}  | {re}  | {b}  | {c}  | {t}  |")
    print(linhaT)
    print(f"B  | {p}  | {p}  | {p}  | {p}  | {p}  | {p}  | {p}  | {p}  |")
    print(linhaT)
    print('C ',linhaL)
    print(linhaT)
    print('D ',linhaL)
    print(linhaT)
    print('E ',linhaL)
    print(linhaT)
    print('F ',linhaL)
    print(linhaT)
    print(f"G  | {p}  | {p}  | {p}  | {p}  | {p}  | {p}  | {p}  | {p}  |")
    print(linhaT)
    print(f"H  | {t}  | {c}  | {b}  | {ra}  | {re}  | {b}  | {c}  | {t}  |")
tabuleiro()

