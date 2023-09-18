larg_aposento = float(input("Digite o comprimento do aposento: "))
comp_aposento = float(input("Digite o comprimento do aposento: "))
altura = 2.80
abertura_porta = 0.80 * 2.10
paredes1 = (larg_aposento * 2.80) * 2
paredes2 = (comp_aposento * 2.80) * 2
total_paredes = (paredes1 + paredes2) - abertura_porta

total_tinta = total_paredes / 3

total_lata = total_tinta / 18
total_galao = total_tinta / 3

print(f"Será necessário {total_tinta:.2f} litros de tinta. {total_lata:.2f} latas de tinta ou {total_galao:.2f} galões de tinta.")
