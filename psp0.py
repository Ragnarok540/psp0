def construir(x, y=None):
    return (x, y)

def lista(*x):
    return construir(x[0], lista(*x[1:])) if x else None

def primero(x):
    return x[0]

def resto(x):
    return x[1]

def vacia(x):
    return x is None

def largo(x):
    return 1 + largo(resto(x)) if not vacia(x) else 0

def sumar(x):
    return primero(x) + sumar(resto(x)) if x else 0

def mapear(f, x):
    return construir(f(primero(x)), mapear(f, resto(x))) if x else None

print(sumar(lista(1, 2, 3)))
print(largo(lista(1, 2, 3)))
print(mapear(lambda x: x - 1, lista(1, 2.5, 3)))
print(vacia(lista()))
