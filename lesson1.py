print ("Hello World")

Tickets_price = 80

if Tickets_price > 80 :
    print("Price greater than 80")
else:
    print("Price less than 80")

#____________________________________________________________

height = int(input("what is your height\n"))
if height >= 120 :
    print("you can ride")
else:
    print("you can't ride")


#____________________________________________________________

integer = int(input("Input number"))

if integer%2 == 0:
    print("even")
else:
    print("odd")

#--------------------

bill = 0
height = int(input("what is your height\n"))
if height >= 120 :
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
     bill = bill+5

    print(f"Your total cost is {bill}")

else:
    print("you can't ride")

