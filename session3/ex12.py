"""
    Veti primi un input de la tastatura, (numar intreg). Folosind acel input,
    va trebui sa afisati o lista cu toate elementele pana la acel numar, daca
    acel numar este par, altfel, veti afisa o lista cu patratele tuturor
    numerelor pana la acel numar.

    exemplu:
        Veti primi 6, veti afisa [1, 2, 3, 4, 5]
        Veti primi 5, veti afisa [1, 4, 9, 16]

"""

x = input("Your input: ")
x = int(x)

numbers=[]

for i in range(1, x):
    if x%2 == 0:
        numbers.append(i)
    else:
        numbers.append(i**2)

print("Output: ", numbers)