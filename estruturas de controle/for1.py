entrada = input("Escreva o numero: ")
entradaFormatada = float(entrada)

print("Soma \n")

for i in range(1, 11):
    print(f"{entradaFormatada} + {i} = {entradaFormatada + i}")

print("Subtração \n")

for i in range(1, 11):
    print(f"{entradaFormatada} - {i} = {entradaFormatada - i}")

print("Multiplicação \n")

for i in range(1, 11):
    print(f"{entradaFormatada} * {i} = {entradaFormatada * i}")

print("Divisão \n")

for i in range(1, 11):
    print(f"{entradaFormatada} : {i} = {entradaFormatada / i}")