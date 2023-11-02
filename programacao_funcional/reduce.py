from functools import reduce

pessoas = [
    {"nome": "Fulano", "idade": 31},
    {"nome": "Cicrano", "idade": 28},
    {"nome": "Deltrano", "idade": 42}
]

soma_idades = reduce(lambda idades, p: idades + p["idade"], pessoas, 0)
print(soma_idades)