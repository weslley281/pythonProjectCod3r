from random import randint

informed_number = -1
secret_number = randint(0, 9)

while informed_number != secret_number:
    informed_number = int(input("Inform a number: "))
    if informed_number < secret_number:
        print("more")
    elif informed_number > secret_number:
        print("less")

print(f"Secret number {secret_number} foi encontrado")