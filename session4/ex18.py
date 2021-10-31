"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""


def f(n):
    if not n:
        return 0
    else:
        return n[0] + f(n[1:])


print(f([4, 5, 7]))
