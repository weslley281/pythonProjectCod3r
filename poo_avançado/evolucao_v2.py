class Humano:
    especie = "Doido"
    def __init__(self, nome: str):
        self.nome = nome

    def do_outro_time(self):
        self.especie = "Do Outro Time"
        return self

if __name__ == '__main__':
    fulano = Humano("Fulano")
    # Humano.do_outro_time(fulano)
    cicrano = Humano("Cicrano").do_outro_time()

    print(f'Especie do humano: {Humano.especie}')
    print(f'Especie do fulano: {fulano.especie}')
    print(f'Especie do cicrano: {cicrano.especie}')
