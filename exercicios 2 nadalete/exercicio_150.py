import math
angulo = float(input("Digite o ângulo em graus: "))
angulo_em_radianos = math.radians(angulo)
quadrante = (angulo_em_radianos // (math.pi / 2)) + 1
if quadrante % 2 == 0:
    resultado = math.sin(angulo_em_radianos)
    print(f"Seno: {resultado:.2f}")
else:
    resultado = math.cos(angulo_em_radianos)
    print(f"Cosseno: {resultado:.2f}")
