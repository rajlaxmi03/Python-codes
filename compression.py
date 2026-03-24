# Program to

#1. Square of numbers 
#Without List Comprehension
sqr = [1, 2, 3, 4, 5]
new_sqr = []
for n in sqr:
    new_sqr.append(n * n)
print(new_sqr)

# with List Comprehension
lcnew_sqr = [n * n for n in sqr]
print(lcnew_sqr)
#2.odd numbers only
#without List comprehension
numbers = [1,2,3,4,5,6,7,8,9]
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print(odd_numbers)
# with List Comprehension
lcodd_numbers = [num for num in numbers if num % 2 != 0]
print(lcodd_numbers)
#3.convert string to uppercase
#without List comprehension
names = ["ram", "sam", "john"]
upper_names = []
for name in names:
    upper_names.append(name.upper())

print(upper_names)

# with List Comprehension
lcupper_names = [name.upper() for name in names]
print(lcupper_names)

#4.Numbers greater than 10
#without List comprehension
gnumbers = [5, 12, 8, 20, 3]
result = []

for num in gnumbers:
    if num > 10:
        result.append(num)
print(result)
# with List Comprehension
result = [num for num in numbers if num > 10]
print(result)
#5.Replace negative numbers with 0
#without List comprehension
negnumbers = [2, -3, 5, -2, 7]
result = []

for num in negnumbers:
    if num < 0:
        result.append(0)
    else:
        result.append(num)
print(result)
#with List comprehension
result = [0 if num < 0 else num for num in numbers]
print(result)
#6. Length of each word
#without List comprehension
words = ["apple", "banana", "kivi"]
lengths = []
for word in words:
    lengths.append(len(word))
print(lengths)
#with List comprehension
lengths = [len(word) for word in words]
print(lengths)

