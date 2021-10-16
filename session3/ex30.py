"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False

"""

data = input()

def parentheses(data):
    stack = []
    dict = {'}':'{',']':'[',')':'('}
    for i in data:
        if i in dict.values():
            stack.append(i)
        elif not stack or dict[i] != stack.pop():
            return False
    if stack:
        return False
    return True

print(parentheses(data))


