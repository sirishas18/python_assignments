import numbers

score_students = [130,140,128.99,159,26,35]

# print(max(score_students))

################# Range ####################
#total = 0
#for number in range(1, 101):
#    total += number
#    print(total)

################# FIZZBUZZ ####################
total = 0

for number in range(1, 101):

    if number%3 == 0 and number%5 == 0:
       print("FizzBuzz")
    elif number % 5 == 0:
       print("Buzz")
    elif number%3 == 0:
        print("Fizz")
    else:
        print(number)

    total += number


###################################

#n = 50
#result = [i for i in range(n) if i%3==0 and i%5==0]
#print(result)