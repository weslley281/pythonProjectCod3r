def converteNota(nota: float):
    if nota > 10:
        return "Nota Inválida"
    elif nota >= 9.1:
        return "Nota A"
    elif nota >= 8.1:
        return "Nota A-"
    elif nota >= 7.1:
        return "Nota B"
    elif nota >= 6.1:
        return "Nota B-"
    elif nota >= 5.1:
        return "Nota C"
    elif nota >= 4.1:
        return "Nota C-"
    elif nota >= 3.1:
        return "Nota D"
    elif nota >= 2.1:
        return "Nota D-"
    elif nota >= 1.1:
        return "Nota E"
    elif nota >= 0:
        return "Nota E-"
    else:
        return "Nota Inválida"


texto: str = input("nota do aluno: ")
print(converteNota(float(texto)))