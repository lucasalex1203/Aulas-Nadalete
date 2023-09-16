saldomedio = float(input("\nDigite o saldo médio: "))
credito = 0.0
if saldomedio <= 500:
    credito = 0.0
elif saldomedio <= 1000:
    credito = saldomedio * 0.3
elif saldomedio <= 3000:
    credito = saldomedio * 0.4
else:
    credito = saldomedio * 0.5
if credito > 0:
    print(f"\nComo seu saldo era de: R${saldomedio:.2f}, seu crédito será de: R${credito:.2f}")
else:
    print(f"\nComo seu saldo era de: R${saldomedio:.2f}, você não terá nenhum crédito.")

