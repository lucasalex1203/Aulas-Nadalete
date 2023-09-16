peso = float(input("Digite o peso (Kg): "))
altura = float(input("Digite a altura (metros): "))
imc = peso / (altura ** 2)
if imc < 20:
    faixa_risco = "Abaixo do peso"
elif 20 <= imc <= 25:
    faixa_risco = "Normal"
elif 25 < imc <= 30:
    faixa_risco = "Excesso de peso"
elif 30 < imc <= 35:
    faixa_risco = "Obesidade"
else:
    faixa_risco = "Obesidade mórbida"
print(f"IMC: {imc:.2f}")
print(f"Faixa de risco: {faixa_risco}")
