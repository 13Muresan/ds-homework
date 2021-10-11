"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'


"""

word = input('Your input: ')
wordL = list(word)

for i in range(len(word)):
    if i % 2 == 0:
        wordL[i] = word[i].upper()
    else:
        wordL[i] = word[i].lower()

print('Output:', ''.join(wordL))





