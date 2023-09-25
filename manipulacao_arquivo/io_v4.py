arquivo = open('pessoas.csv')

try:
    for registro in arquivo:
        dado = registro.strip().split(',')
        print(f'Nome: {dado[0]}, Idade: {dado[1]}')
finally:
    arquivo.close()