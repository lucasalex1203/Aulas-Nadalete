import math as m
n=int(input('\nEntre com um número de 3 dígitos: '))
c=n/100
d=n%100/10
u=n%10
n=u*100+d*10+c
print(f'\nNumero: {n} ')
print(f'\nInvertido: {n} ')
print('\n')