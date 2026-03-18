t = (1,3,6)
print(t)
#HETEROGENOUS DATA
t1 = ("gamana", 5.4, 100, 'a')
print(t1)
#SINGLE VALUE INSIDE A TUPLE  YOU NEED TO PROVIDE (3, )
t2 = (3)
print(t2)
#TYPE OF VALUE
t3 = (3, )#COMA IS GIVEN TO MAKE IT TUPLE TYPE NOT INTEGER
print(type(t3))
#       0        1    2    3
t4 = ("gamana", 5.4, 100, 'a')
print(t4[2])  #INDEX VALUE
print(t4[0])

#in reverse order acces
#     -4         -3   -2   -1
t5 = ("gamana", 5.4, 100, 'a')
print(t5[-2])  #INDEX VALUE
print(t5[-4])

t6 = (1, 3, 6, 7, 8)
print(t6[1:4])
print(t6[:3])

#OPERATIONS
tup = (1,2,3,4)
print(len(tup))   #4
#CONCATENATION
print(t1 + tup)
#REPAEATING A TUPLE
t7 = (3) * 3 #MULTIPLICATION OPERATOR
print(t7)

#RETURN MULTIPLE VALUES USING RETURN KEYWORD
def name():
    n1 = "Gamana"
    n2 = "Nithin"
    n3 = "Geetha"
    return (n1, n2, n3)
print(name())

#Packing
student = ('Ravi', 20, 'Physics')
print(student)

#unpacking
name, age, course = student # from student you are splitting up
print(name)
print(age)
print(course)
