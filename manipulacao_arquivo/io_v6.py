with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            dado = registro.strip().split(',')
            print(f'Nome: {dado[0]}, Idade: {dado[1]}', file=saida)

if arquivo.close():
    print("Arquivo foi fechado")