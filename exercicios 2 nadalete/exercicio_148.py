def calcular_preco(destino, ida_e_volta):
    if destino == "Regiao Norte":
        if ida_e_volta == 1:
            return 500.00
        else:
            return 900.00
    elif destino == "Regiao Nordeste":
        if ida_e_volta == 1:
            return 350.00
        else:
            return 650.00
    elif destino == "Centro-Oeste":
        if ida_e_volta == 1:
            return 350.00
        else:
            return 600.00
    elif destino == "Regiao Sul":
        if ida_e_volta == 1:
            return 300.00
        else:
            return 550.00
    else:
        return -1.0
print("\nDigite 1- Regiao Norte 2- Regiao Nordeste 3- Regiao Centro-Oeste 4- Regiao Sul:")
op = int(input())
print("\nDigite 1- Ida 2- Ida e Volta:")
iv = int(input())

destinos = {
    1: "Regiao Norte",
    2: "Regiao Nordeste",
    3: "Centro-Oeste",
    4: "Regiao Sul"
}

destino_escolhido = destinos.get(op)

preco = calcular_preco(destino_escolhido, iv)

if preco == -1.0:
    print("\nOpção Inexistente")
else:
    print(f"\nO valor da passagem é: R${preco:.2f}")
