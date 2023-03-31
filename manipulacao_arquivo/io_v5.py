with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        dado = registro.strip().split(',')
        print(f'Nome: {dado[0]}, Idade: {dado[1]}')

if arquivo.close():
    print("Arquivo foi fechado")