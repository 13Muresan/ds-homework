"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1

"""

x = input("Your input: ")

count=0

for char in x:
    if char in 'aeiouAEIOU':
        count += 1

print("Output: ", count)