#print("Enter name:")
#name = input()
#print(f "My name is {name}")
name = input("Enter name:")
print("My name is" + name)
# to add two numbers

a = int(input("Enter number 1: "))
b = int(input("Enter number2: "))
print(f"The number a is {a}")
print(f"The number b is {b}")
print(f"Addition of a + b is {a + b}")

# TODO: Prompt the user to enter their name and store it in user_name
user_name = input();


# TODO: Prompt the user to enter the number of items they plan to purchase and store it in items_count
items_count = int(input());
# TODO: Prompt the user to enter their total budget for shopping and store it in total_budget
total_budget = float(input());
# TODO: Prompt the user to confirm if they have a discount coupon and store it in has_coupon
has_coupon = bool(input());
# TODO: Print a summary of the collected user information
print("Grocery Shopping Summary:");
print(f"Name: {user_name}");
print(f"Number of items: {items_count}");
print(f"Total budget: $ {total_budget}");