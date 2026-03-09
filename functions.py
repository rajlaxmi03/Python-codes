# add 2 numbers
#function declaration
def add():
    a = 10
    b = 20
    print(a + b)
add()  # function call

#square 
def square():
    c = 10
    print(c * c)
square()

# largest among 3 numbers
def largest():
    a = 10
    b = 20
    c = 30
    if (a > b and a > c):
        print(a)
    elif (b > a and b > c):
        print(b)
    else:
        print(c)
largest()
