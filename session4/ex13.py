"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""
def myfunc1(arg):
    result=''
    func = arg()
    for i in range(0, len(func)):
        if i % 2 == 0:
            result += func[i].upper()
        else:
            result += func[i].lower()
    print(result)


# decorate me
@myfunc1
def f():
    return 'cmi'

