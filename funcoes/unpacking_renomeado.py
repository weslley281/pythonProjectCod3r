# **kwargs
def resultado_f1(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'1) {segundo}')
    print(f'1) {terceiro}')

podium = {
    'segundo': 'Cicrano',
    'terceiro': "Deltrano", 
    'primeiro': 'Fulano'
}

resultado_f1(**podium)

