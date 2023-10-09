compras = (
    {"quantidade": 2, "valor": 10},
    {"quantidade": 3, "valor": 20},
    {"quantidade": 5, "valor": 14},
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['valor'],
        compras
    )
)

print("Preços totais: ", totais)
print("Total geral: ", sum(totais))