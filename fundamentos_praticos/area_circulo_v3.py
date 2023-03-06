from math import pi
from math import pow

raio = input('Informe o raio: ')
print('Area do circulo', pi * float(raio) ** 2)

numero = input('Digite um numero')
potencia = input('Elevado a quantos')
print(f'{numero} elevado a {potencia} é igual a {pow(float(numero), float(potencia))}')

print('Nome do modulo', __name__)
print('Nome do pacote', __package__)