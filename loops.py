#loops in python
#FOR
for i in range(5):
    print(i)

#WHILE
i = 0
while i <= 4:
    print(i)
    i += 1

#even number
for num in range(1, 11):
    if num % 2 == 0:
        print(num, end=" ")

#looping for
for i in range(0, 11,2):
    print(i)

for num in range(1, 11):
    if num % 2 == 0:
        print(num, end=" ")


        # jump control statements 1-6
#break
for i in range(1, 6):
    if i == 4:
        break
    print(i)

#Continue
for i in range(0, 6):
    if i == 4:
        continue
        print(i)

#square of number
def square(n):
    return n * n
print(square(4))

#pass
for i in range(0, 6):
    pass

def add():
    pass
add()