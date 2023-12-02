
Y = 22
totalCabecas = int(input('Digite o total de cabeças: '))
# Y * 2 + 5 = 49
totalPes = int(input('Digite o total de pés: '))
# Y * 3 + 7 = 73

def peCabeca(cabecas, pes):
    for patos in range(0, cabecas + 1):
        coelhos = cabecas - patos
        if (2 * patos) + (4 * coelhos) == pes:
            return patos, coelhos
    else:
        return False, False

#Tenho 49 cabeças e 73 pés segundo sua fórmula, sendo impossivel uma resolução.\
patos, coelhos = peCabeca(totalCabecas, totalPes)

if patos == False:
    print(f'Nâo existe solução possivel')
else:
    print(f'total de patos é {patos}, total de coelhos é {coelhos}')
