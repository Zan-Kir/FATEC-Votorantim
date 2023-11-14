#def valida_cpf():
cpf = input('Digite o cpf no formato xxx.xxx.xxx-xx: ')
cpf_numeros = ''.join(filter(str.isdigit, cpf))
acumulador1 = 0
acumulador2 = 0
contador = 10
contador2 = 11
valido = 0

if len(cpf_numeros) != 11:
    return False

if cpf_numeros == cpf_numeros[0] * 11:
    return False

for i in range(0, 3):
    acumulador1 = acumulador1 + (int(cpf[i]) * contador)
    acumulador2 = acumulador2 + (int(cpf[i]) * contador2)
    contador = contador - 1
    contador2 = contador2 - 1
for i in range(4, 7):
    acumulador1 = acumulador1 + (int(cpf[i]) * contador)
    acumulador2 = acumulador2 + (int(cpf[i]) * contador2)
    contador = contador - 1
    contador2 = contador2 - 1
for i in range(8, 11):
    acumulador1 = acumulador1 + (int(cpf[i]) * contador)
    acumulador2 = acumulador2 + (int(cpf[i]) * contador2)
    contador = contador - 1
    contador2 = contador2 - 1

print(acumulador1 % 11)

if acumulador1 % 11 < 2:
   if cpf[12] == 0:
    valido = valido + 1
if acumulador2 % 11 < 2:
    if cpf[13] == 0:
        valido = valido + 1
else:
    dig1 = acumulador1

#if valido == 2:
    #return True
#else:
    #return False