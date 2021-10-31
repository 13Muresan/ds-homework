"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'

"""

import string

alphabet = string.ascii_lowercase


def func(result=''):
    shift = 1
    result = ''.join(map(lambda x: chr((ord(x) - 97 + shift) % 26 + 97) if x in alphabet else x, result.lower()))
    return result


print(func('xyz'))
