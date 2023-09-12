x = float(input("Digite um valor para x: "))
y = float(input("Digite um valor para y: "))
z = float(input("Digite um valor para z: "))

if x + y > z and y + x > z and z + y > x:
    e_triangulo = f"Ele é um triângulo "
    if (x == y) or (x == z) or (y == z):
        tipo = "Isóceles"
    elif (x == y) and (x == z):
        tipo = "Equilátero"
    elif (x != y != z):
        tipo = "Escaleno"
else:
    e_triangulo = f"Ele não é um triangulo"
print(f"{e_triangulo}{tipo}")
