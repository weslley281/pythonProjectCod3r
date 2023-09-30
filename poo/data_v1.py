class Data:
    def __init__(self, dia: int = 28, mes: int = 11, ano: int = 2023):
        self.dia: int = dia
        self.mes: int = mes
        self.ano: int = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

data1 = Data(5, 12)
print(data1)

data2 = Data(28, 11, 2023)
# data2.dia = 28
# data2.mes = 11
# data2.ano = 2023

print(data2)

