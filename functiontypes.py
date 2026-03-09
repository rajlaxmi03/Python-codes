#No arguments  + No return Value
def add():
    a = 30
    b = 20
    print(a + b)
add()

#No arguments + Return value
def add():
    c = 10
    d = 10
    return (c + d)
print(add())

#Arguments + No return Value
def add(x, y):
    print(x + y)
add(100, 200)

#Arguments + Return Value
def add(p, q):
    return p + q
res = add(200, 300)
print(res)

# PRINT CUBE OF NUMBER IN ALL 4 WAYS

def cube1():
    a = 8
    print(a * a * a)
cube1()


def cube2():
    b = 5
    return b * b * b
print(cube2())


def cube3(c):
    print(c*c*c)
cube3(11)


def cube4(d):
    return d * d * d
print(cube4(20))

