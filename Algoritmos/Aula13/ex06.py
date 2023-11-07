def convertSeg(hora, min, seg):
    totalSeg = ((hora * 60) * 60) + (min * 60) + seg
    return totalSeg

h = int(input("Digite a hora: "))
m = int(input("Digite os minutos: "))
s = int(input("Digite os segundos: "))

print(f"O total de segundos é {convertSeg(h, m, s)}.")