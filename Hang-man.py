import random
word_list = ["daisey", "hibiscus", "rose"]

# Todo-1: Randomly choose a word and assign it to choosen word and print it
# Todo-2: Ask user to guess word and assign it to variable guess_lowercase
# Todo-3: Check guessed letter is from the choosen word and print right or wrong
# Corrections to steps 1,2,3 follows
# Todo-4: Create a placeholder with same no of blanks as chosen_word
# Todo-5: Create a "display" that puts guess letter in right position and "-" in rest
# Todo-6: use a while loop to guess another letter again
# Todo-7: Change the for loop to keep previous correct and letter in display
# Todo-8: create variable "lives"-to keep track of
# Todo-9: any guess letter is not in choosen letter than reduce "lives" by 1
# Todo-10: Print the ASCII art farm stages - corresponding to lives

Choosen_word = random.choice(word_list)
print(Choosen_word)

placeholder = ""
word_length = len(Choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letter = []

lives = word_length

while not game_over:
    guess = input("Guess a letter from the word? : \n ").lower()

    display = ""
    for letter in Choosen_word:
        if letter == guess :
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in Choosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("You guessed the right word.")




