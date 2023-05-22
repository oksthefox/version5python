#!/usr/bin/python3
import random
import sys

# function for picking random word from a file
def randomword(file):
    with open(file,'r') as f:
        file_content = f.read()
        list_of_words =file_content.split()
        the_word = random.choice(list_of_words)
        random_word = the_word.lower()
        print("Welcome to Hangman!")
        print("You can be wrong up to 5 times")
#        print(random_word)
        list_of_letters = []
        for i in random_word:
            list_of_letters.append(i)
#        print(list_of_letters)
        length = len(random_word)

    display_word = ['_']*length
    print(' '.join(display_word))
# the user guess a letter of the word, if the letter already in the list it won't adds it
    guessedletter=[]
    incorrect_guess = 0

    while '_' in display_word and incorrect_guess < 5:
        gussletter = input("Guess your letter: ")
        if gussletter in guessedletter:
            print("you alredy guessed that letter!")
        else:
            guessedletter.append(gussletter)
            correct_guess = False
            for i in range(length):
                if random_word[i] == gussletter:
                    display_word[i]=gussletter
                    correct_guess = True
            if correct_guess:
                print("correct guess!")
            else:
                print("incorrect guess!")
                incorrect_guess += 1
                if incorrect_guess == 5:
                    break
        print(' '.join(display_word))
    if '_' in display_word:
        print("you lost! you made 5 incorrect guesses")
        print("the word was " + random_word+"!")
    else:
        print("well done!you guessed the word correctly!")




    #main code

randomword(sys.argv[1])

