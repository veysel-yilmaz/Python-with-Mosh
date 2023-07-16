# finds kg value if k is chosen, finds lbs value if l is chosen
"""weight = input("What is your weight: ")
type = input("(L)bs or (K)g: ")
if type == 'k' or type == 'K':
    print("You are" + weight * 2.2 + "pounds.") # !!!weight is a string value and cannot be multiplied by a number.
elif type == 'l' or type == 'L':
    print("You are" + weight / 2.2 + "kilograms.")
else:
    print("Please enter correct weight type." """
#answer:
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")