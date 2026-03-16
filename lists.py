#Lists - COLLECTIONS OF MULTIPLE VALUES STORED IN A SINGLE VARIABLE
# ORDERED, MUTABLE, ALLOW DUPLICATES , []

#printing the list
number = [10, 20, 30, 40]
print(number)

#can list store various data types\\ Heterogenous data
data = [10, 34.5, "Gamana", True]
print(data)

#how to access elements in list (ACCESSING DATA)
print(data[2])
#insert any value
data[2] = "chandu"
print(data)

#Add Elements inside list
numbers = [10, 20, 30, 40]
print(numbers)
numbers.append(60)
print(numbers)
#in case in middle 
numbers.insert(1, 70)
print(numbers)
#Remove Elements
numbers.remove(70)#value
print(numbers)
numbers.pop(4)#index
print(numbers)

print(len(numbers))
