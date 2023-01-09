lista = []
print(type(lista))
print(dir(list))
print(len(lista))
lista.append(1)
lista.append(2)
print(lista)
print(len(lista))

nova_lista = [lista, 'Ana', 'Bia']
print(nova_lista)
nova_lista.remove('Ana')
print(nova_lista)
