print("-------------------------------------------------")
print("************* WELCOME TO PIZZA SHOP *************")
print("-------------------------------------------------")
print(" ")
pizza_size = input("Choose size of the pizza? S, M, L? ").upper()
add_pepperoni = input("Do you want to add pepperoni? Y or N? ").upper()
extra_cheese = input("Do you want to add extra cheese? Y or N? ").upper()

bill = 0

if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is: ${bill}")
