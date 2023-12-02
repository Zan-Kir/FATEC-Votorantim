
Y = 22
totalCabecas = Y * 2 + 5
totalPes = Y * 3 + 7

def peCabeca(cabecas, pes):
    for patos in range(0, cabecas + 1):
        coelhos = cabecas - patos
        if (2 * patos) + (4 * coelhos) == pes:
            return patos, coelhos
    else:
        return False

#Tenho 49 cabeças e 73 pés segundo sua fórmula, sendo impossivel uma resolução.\
patos, coelhos = peCabeca(totalCabecas, totalPes)

if peCabeca(totalCabecas, totalPes) == False:
    print(f'Nâo existe solução possivel')
else:
    print(f'total de patos é {patos}, total de coelhos é {coelhos}')
