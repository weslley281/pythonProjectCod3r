# **kwargs
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')

resultado_f1(primeiro = 'Fulano', segundo = 'Cicrano', terceiro = "Deltrano")

