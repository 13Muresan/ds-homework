"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""
import random

x = input("Your number:")
x = int(x)

result = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k = x))

print("The generated random string : ", result)