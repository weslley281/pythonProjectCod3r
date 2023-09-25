arquivo = open('pessoas.csv')

for registro in arquivo:
    dado = registro.strip().split(',')
    print(f'Nome: {dado[0]}, Idade: {dado[1]}')