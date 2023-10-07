class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')

class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')

class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teias', 'andar nas paredes')

class HomenAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ('combater o crime',)

if __name__ == '__main__':
    fulano = Homem()
    print(f"Fulano: {fulano.capacidades}")

    aranha = Aranha()
    print(f"Aranha: {aranha.capacidades}")

    cicrano = HomenAranha()
    print(f"Homem-Aranha: {cicrano.capacidades}")
