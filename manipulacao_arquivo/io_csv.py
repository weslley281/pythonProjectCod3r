import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print(f'Nome: {pessoa[0]}, Idade: {pessoa[1]}')