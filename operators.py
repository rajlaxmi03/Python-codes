# Arithmetic operation
number_of_samosas = 5
price_per_samosa = 10
total_earnings = number_of_samosas * price_per_samosa
print("Total earnings from samosas:", total_earnings)

my_samosas = 5
priya_samosas = 7
print("Did Priya make more samosas than me?", priya_samosas > my_samosas)
age = 20
has_pass = True
can_enter = age > 18 and has_pass
print("Can Ramesh enter the club?", can_enter)
total_earnings = 50
total_earnings += 30  # This is like saying: total_earnings = total_earnings + 30
print("Total earnings after two days:", total_earnings)
A = 1  # ON
B = 0  # OFF
result = A & B  # Both need to be ON for result to be 1

print("Are both switches ON?", result)


# Program to Explain Python Operators


print("----- Arithmetic Operators -----")


a = 10
b = 3


print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.333333
print("Floor Division:", a // b)   # 3
print("Modulus:", a % b)           # 1
print("Power:", a ** b)            # 1000



print("\n----- Comparison Operators -----")


x = 5
y = 10


print("x > y :", x > y)     # 
print("x < y :", x < y)     # 
print("x == y :", x == y)   # 
print("x != y :", x != y)   # 
print("x >= y :", x >= y)   # 
print("x <= y :", x <= y)   # 



print("\n----- Logical Operators -----")


p = True
q = False


print("p and q :", p and q)   # False
print("p or q :", p or q)     # True
print("not p :", not p)       # False



print("\n----- Assignment Operators -----")


num = 10
print("Initial value:", num) #10


num += 5
print("After += :", num) #num = num + 5 = 15


num -= 3
print("After -= :", num) # num = 15 - 3 = 12


num *= 2
print("After *= :", num) # num = 12 * 2 = 24


num //= 4
print("After //= :", num) # 24 / 4 = 6



print("\n----- Identity Operators - Content -----")


a = 5
b = 5
c = 10


print("a is b :", a is b)
print("a is c :", a is c)
print("a is not c :", a is not c)

print("\n----- Membership Operators -----")


numbers = [1, 2, 3, 4, 5]


print("3 in list :", 3 in numbers)
print("10 in list :", 10 in numbers)
print("10 not in list :", 10 not in numbers)


print("\n----- Bitwise Operators -----")
a = 5
b= 3


print(a & b) # 1
print(a | b) # 7
print(a ^ b) # 6
print(~a) #-6
print(5<<1) #10
print(5>>1) #2
