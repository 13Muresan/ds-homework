"""
    Ex. 19: Scrieti o functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el
    un dictionar de 4 elemente aleatoare unde key = int, iar value = string,
    iar stringul sa aiba intre 3 si 6 caractere si key sa fie intre 0 si 10.

    Exemplu:
        f('ceva')
        ---> generez ceva.json ca si fisier
        ---> generez un dictionar
            {
                1: 'blabla',
                5: 'cmi',
                7: 'cmi22',
                10: 'balqef'
            }


"""

import json
import random
from random import choice
from string import ascii_lowercase


def f(n):

    listofStrings = [''.join(choice(ascii_lowercase) for _ in range(3,7)) for _ in range(4)]
    listofInts = random.sample(range(0, 11), 4)
    dict_1 =  dict( zip(listofInts, listofStrings))

    with open("n.json", "w") as outfile:
        json.dump(dict_1, outfile)

    return dict_1


f("ceva")

