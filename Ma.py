import math

radius = int(input("Zadej poloměr: "))
height = int(input("Zadej výšku: "))

def plocha_kruhu(radius):
    return math.pi * (radius ** 2)

def objem_koule(radius):
    return (4/3) * math.pi * (radius ** 3)

def objem_válce(radius, height):
    return math.pi * (radius ** 2) * height

def objem_kuželu(radius, height):
    return (1/3) * math.pi * (radius ** 2) * height

print("Plocha kruhu: ", plocha_kruhu(radius))
print("Objem koule: ", objem_koule(radius))
print("Objem válce: ", objem_válce(radius, height))
print("Objem kuželu: ", objem_kuželu(radius, height))