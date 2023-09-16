import math
x = float(input("Digite o valor de x: "))
if x > 4 or x < -4:
    fx = (5 * x + 3) / math.sqrt(x**2 - 16)
    print(f"\nf(x) = {fx}")
else:
    print("\nNÃO PODE SER FEITA")
