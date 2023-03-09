produto = {
    'nome': 'Chuca Gostosa',
    'importada': True,
    'valor': 34.99,
    'estoque': 800
}

for chave in produto.keys():
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f"{chave} = {valor}")