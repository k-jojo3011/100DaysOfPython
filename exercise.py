print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want ? S, M, or L:").upper()
add_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N:").upper()

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25


if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    if size == "S":
        bill += 1
print(f"Your final bill is: ${bill}")


