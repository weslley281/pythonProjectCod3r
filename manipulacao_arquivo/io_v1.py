arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    dado = registro.split(',')
    print(f'Nome: {dado[0]}, Idade: {dado[1]}')