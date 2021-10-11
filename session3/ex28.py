"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati suma numerelor pana la numarul respectiv.

    exemplu:
        Veti primi: 5
        Veti printa: 15
"""
x = input("Your input: ")
x = int(x)

print("Sum:", sum(range(0, x+1)))