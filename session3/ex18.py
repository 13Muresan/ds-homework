"""
    Veti primi un string de la tastatura.
    Veti primi doua numere intregi de la tastatura, x, y.
    Va trebui sa printati substringul de la indexul x la indexul y (inclusiv).

    exemplu:
        Veti primi: 'Center for Intelligent Machines', 2, 5
        Veti printa: 'nter'
"""
word = input("Your Sentences: ")
x = input("x: ")
y = input("y: ")


x = int(x)
y = int(y)
print("Output: ", word[x:y+1])