word = "So Cute"
for letter in word:
    print(letter, end=".")

print("\n")

peoples = ["Fulano", "Cicrano", "Deltrano"]
for name in peoples:
    print(name, end=", ")

print("\n")

for position, name in enumerate(peoples):
    print(f"{name} is in the position {position}")

print("\n")

week_days = ("Sunday", "Monday", "Tuesday", "Thursday", "Friday", "Saturday")
for day in week_days:
    print(f"Today is {day}")