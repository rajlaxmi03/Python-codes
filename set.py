# A Set in Python is a collection of unique (no duplicate ) elements
#No duplicate values
#Unordered(no indexing like lists)
#mutable (you can add/ remove items)
#Fast operations (like membership check)

#Using curly braces{}
my_set = {1, 2, 3, 4}
print(my_set)

#using set function
another_set = set((1, 2, 2, 3))  #duplicate remove
print(another_set)  # output : {1,2,3}

#add
s = {1, 2, 3}
s.add(4)
print(s) #{1,2,3,4}

#Remove elements
s.remove(2)  #Error if not found
s.discard(10)  #No error if not found

#Check Membership
print(3 in s)  #True

#Set operations
# union  (combine sets)
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) # {1,2,3,4,5}

#Intersection (common elements)
print(a & b)  #{3}


#Difference {Elements in a but not in b}
print(a - b)   # {1,2}

#Symmetric Difference 
print(a ^ b)

for item in a:
    print(item)

numbers = {1, 2, 3, 4, 4, 5}
unique_numbers = set(numbers)
print(unique_numbers)
