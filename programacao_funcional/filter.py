pessoas = [
    {"nome": "Fulano", "idade": 31},
    {"nome": "Cicrano", "idade": 28},
    {"nome": "Deltrano", "idade": 42},
    {"nome": "Maltrano", "idade": 12},
    {"nome": "Heltrano", "idade": 8}
]

menores = filter(lambda p: p["idade"] < 18, pessoas)
print(list(menores))
