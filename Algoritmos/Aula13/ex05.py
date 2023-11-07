from math import pow, pi
def volEsfera(raio):
    return ((4 / 3) * pi * pow(raio, 3))

r = float(input("Entre com o valor do raio: "))

print(f"O valor da esfera é {volEsfera(r):.2f}m³.")
