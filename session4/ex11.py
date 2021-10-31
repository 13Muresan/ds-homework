"""
    Ex. 11: Scrieti un decorator care sa logheze outputul unei functii
    pe care o decoreaza, intr-un fisier "output11.data".

    https://www.w3schools.com/python/python_file_write.asp

    Functia decorata este f.
"""


def dec(func):
    def myfunc():
        x = func()
        y = open("output11.data", "a")
        y.write(x)
        y.close

    return myfunc


# decorate me
@dec
def f():
    return "CMI"


f()
