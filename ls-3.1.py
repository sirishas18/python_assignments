cost = 0
bill = 0
print("Order your Pizza")
size = input("What size of Pizza do you want? s, m or l: \n ")
if size == "s":
    cost = 15
    print("Plz pay $15")
    Pepperoni = input("Do you want to add pepperoni? y or n : \n")
    if Pepperoni == "y":
        bill = cost + 2
    else:
        bill = cost
        print(f"Your total cost is {bill}")
    Cheese = input("Do you want extra cheese? y or n : ")
    if Cheese == "y":
        bill = bill + 1
    else :
        bill = bill
    print(f"Your total cost is {bill}")

elif size == "m":
    cost = 20
    print("Plz pay $20")
    Pepperoni = input("Do you want to add pepperoni? y or n : \n")
    if Pepperoni == "y":
        bill = cost + 2
    else:
        bill = cost
        print(f"Your total cost is {bill}")
    Cheese = input("Do you want extra cheese? y or n : ")
    if Cheese == "y":
        bill = bill + 1
    else :
        bill = bill
    print(f"Your total cost is {bill}")

elif size == "l":
    cost = 25
    print("Plz pay $25")
    Pepperoni = input("Do you want to add pepperoni? y or n : \n")
    if Pepperoni == "y":
        bill = cost + 3
    else:
        bill = cost
        print(f"Your total cost is {bill}")
    Cheese = input("Do you want extra cheese? y or n : ")
    if Cheese == "y":
        bill = bill + 1
    else :
        bill = bill
    print(f"Your total cost is {bill}")

else:
    print("You\'ve select wrong option.Plz select s or m or l")

#.lower()
# pseudoramdom number generators