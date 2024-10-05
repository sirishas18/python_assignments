import random

#random_integer = random.randint(1,10)
#print(random_integer)

#random_dice = random.randint(0,1)
#print(random_dice)

#if random_dice ==1 :
#    print("Heads")
#else:
#    print("Tails")

####################LIST############################
##LIST.append ##########################

friends = ["James","Alice", "Abhi", "Ram", "Kaushik"]

random_name = random.randint(0,4)
print(random_name)
if random_name ==0 :
    print("James")
elif random_name == 1:
        print("Alice")
elif random_name == 2:
        print("Abhi")
elif random_name == 3:
        print("Ram")
else:
    print("Kaushik")

#################  (or) do above program as below  ############################

friends = ["James","Alice", "Abhi", "Ram", "Kaushik"]

print(random.choice(friends))

#################  (or) do above program as below  ############################

random_name = random.randint(0,4)
print(friends[random_name])

#############################################

states_of_Australia = ["Vic", "NSW", "Brisbane"]
print(len(states_of_Australia))
#############################################

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
# list 1 of 2nd item
print(dirty_dozen[1][3])

print(dirty_dozen[1][1])

##########################################################
