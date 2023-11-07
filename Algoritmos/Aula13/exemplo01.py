# Definição de Funções
qnt= 5
x = 10

def linha(qnt=20):
    print(qnt, "dentro", x)
    for i in range(0,qnt):
        print("-", end='')
    print()

linha()
linha(25)
print(qnt, "fora", x)
print("** Uso de Funções **")
linha(30)