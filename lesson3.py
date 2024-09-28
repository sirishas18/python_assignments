bill = 0
height = int(input("what is your height\n"))
if height >= 120:
    print("you can ride")
    age = int(input("what is your age\n"))
    if age <= 12:
        bill = 5
        print("Plz pay $5-child")
    elif age <= 18:
        bill = 7
        print("Plz pay $7-youth")
    else:
        bill = 12
        print("Plz pay $12")

    want_photo = input("do you want to take PIC? y/n\n")
    if want_photo == "y":
        bill = bill + 5

    print(f"Your total cost is {bill}")

else:
    print("you can't ride")

