na=float(input(f'\nHoras trabalhadas: '))
vha=float(input(f'\nValor da hora-aula: '))
pd=float(input(f'\nPercentual de desconto: '))
print('\n')
sb=na*vha
print('\n')
td=(pd/100)*sb
print('\n')
sl=sb-td
print(f'\nSalário líquido: {sl}')
print('\n')
