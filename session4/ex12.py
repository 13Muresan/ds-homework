"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""


def dec(func):
    def myfunc(args):
        func(args)
        y = open("output12.data", "a")
        y.write(str(func(args)))
        y.close

    return myfunc


# decorate me
@dec
def f(x):
    print(x)


print(f("cmi"))
