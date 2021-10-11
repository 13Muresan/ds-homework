"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
x = input("Your word:")
x = str(x)

vocale=0
consoane=0

for char in x:
    if char in 'aeiouAEIOU':
        vocale += 1
    else: consoane += 1

print (f"Your word has {vocale} vowels and {consoane} consonants.")