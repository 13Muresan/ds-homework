"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa spuneti daca acel numar este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: numarul este acelasi de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 12321
        Veti printa: True

        Veti primi: 1232
        Veti printa: False
"""

x = input("Write your number here:  ")

if str(x) == str(x)[::-1]:
    print("True")
else:
    print("False")