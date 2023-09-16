n=float(input('\nEntre com um número com parte fracionária: '))
ni=int(n-0.5)
nfrac=n-ni
na=int(n+0.00001)
print(f'\nParte inteira: {ni}')
print(f'\nParte fracionária: {(nfrac+0.00001):.3f}')
print(f'\nParte arredondado: {na}')
print('\n')