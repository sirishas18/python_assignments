import numbers
import random
import string



letter_l = list(string.ascii_lowercase)
letter_u = list(string.ascii_uppercase)
letters = letter_l + letter_u
print(letters)
#print(string.ascii_letters)
#string.digits
numbers = ('0','1','2','3','4','5','6','7','8','9')
#string.punctuation
symbol = ("!","@","#","$","%","^","&","*")

nr_letters = int(input("How may letter would you like in password\n"))
nr_numbers = int(input("How may numbers would you like in password\n"))
nr_symbols = int(input("How may symbols would you like in password\n"))

password = ""

for char in range(1,nr_letters+1):
    password += random.choice(letters)
    #print(password)
for char in range(1,nr_numbers+1):
    password += random.choice(numbers)
    #print(password)
for char in range(1,nr_symbols+1):
    password += random.choice(symbol)
    #print(password)
print(password)

random.shuffle(password)





