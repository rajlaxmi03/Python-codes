#IF Statements
# To check if a person is eligible to vote
age  = 19
if age >= 18:
    print("Eligible to vote")
    print("Thank You")

# IF ELSE
age = 19
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
    print("Thank You")

#ELIF   (IF - ELIF - ELSE)
#To check multiple conditions
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("fail")

#Nested if
free_tonight = True
friends_available = False

if free_tonight:
    if friends_available:
        print("Go out for dinner with friends!")
    else:
        print("Order food and watch a movie.")
else:
    print("Continue with assignments.")

    #match
day = 3
match day:
    case 1: print("Mon")
    case 2: print("Tue")
    case 3: print("Wed")
    case 4: print("Thu")
    case _: print("Invalid day")

# default is not written it is written as underscore(_)
day = 6
match day:
    case 1: print("Mon")
    case 2: print("Tue")
    case 3: print("Wed")
    case 4: print("Thu")
    case _: print("Invalid day")

month = 4
match month:
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8:
        print("Rainy")
    case 9 | 10 | 11 | 12:
        print("Winter")
    case _: print("invalid")
