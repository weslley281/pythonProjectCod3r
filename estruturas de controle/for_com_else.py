ASSUNTOS_PROIBIDOS = ('futebol', 'religião', 'politica')
textos = [
    "João gosta de futebol",
    "A praia foi top"
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in ASSUNTOS_PROIBIDOS:
            print("Texto possui assuntos proibido: ", palavra)
            break
    else:
        print("Texto autorizado: ", texto)