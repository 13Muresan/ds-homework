"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti daca acel string este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: stringul se citeste la fel de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 'center'
        Veti printa: False

        Veti primi: 'cojoc'
        Veti printa: True
"""

x = input("Write your word here:  ")

if str(x) == str(x)[::-1]:
    print("True")
else:
    print("False")