def cores_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'roxo'
    yield 'verde'
    yield 'azul'
    yield 'branco'
    yield 'lilas'
    yield 'magento'
    yield 'ciano'

if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    while True:
        print(next(generator))