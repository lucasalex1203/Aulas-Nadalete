import math as m
sm=int(input('\nEntre com o salário mínimo: '))
quantidade=int(input('\nEntre com a quantidade de quilowatt: '))
preço=sm/700
vp=preço*quantidade
vd=vp*0.9
print(f'\nPreço do quilowatt:{preço}\nValor a ser pago: {vp}\nValor com desconto: {vd} ')
print('\n')