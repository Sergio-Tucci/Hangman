import random
from hangman_words import word_list
from hangman_art import stages, logo

# up to here, imports necessary for the project, random, list of words and stage of the hanged man

lives = 6 # quantity of lives the user has at the beginning of the program

print(logo) # print the logo of the game
chosen_word = random.choice(word_list) # pick a word from the word list to be the chosen one
print(chosen_word) # print the chosen work

placeholder = "" # variable created to print the blank spaces
word_length = len(chosen_word) # variable to store the chosen word length
for position in range(word_length): #looping through the length to display the same name of blank space as _
    placeholder += "_" # store as many _ as needed to reach the chosen word length
print("Word to guess: " + placeholder) #print underscores

game_over = False # variable to store a boolean value for future check
correct_letters = [] # list to store the correct guessed letters

while not game_over: # while loop to keep the program running till game_over become True


    print(f"****************************{lives}/6 LIVES LEFT****************************") #display number of life thar user has
    guess = input("Guess a letter: ").lower() # request the user to guess a letter and store it into a variable


    if guess in correct_letters: # if condition to check if the user has already used the same letter before to proceed without loosing life
        print(f"You've already guessed {guess}") # print to inform that he has used this letter before

    display = "" # variable created to store display progress

    for letter in chosen_word: # looping through chosen word to check if guessed letter match with any of them
        if letter == guess: # compare if a letter from chosen word is iqual guessed word
            display += letter # store the wright letter into display
            correct_letters.append(guess) # use appending to bring the letter to the list correct_letters
        elif letter in correct_letters: #check if it has a letter in correct_letters
            display += letter #store letter and keep the progress
        else: # don't have the letter in chosen word
            display += "_" #add underscore to show the user their progress

    print("Word to guess: " + display) #print display


    if guess not in chosen_word: #chack if guessed letter is not in chosen word
        lives -= 1 # subtract 1 life from the total of lives
        print(f"You guessed {guess}, that's not in the word. You lose a life.") #print to inform that user misses the word and loses a life
        if lives == 0: # check if the quantity of life is iqual 0
            game_over = True # if iqual 0, it means that user loses the game / changes boolean value to finish while looping

            print(f"***********************YOU LOSE**********************")
            print(f"The correct word was {chosen_word}") #show the user the chosen word after losing game

    if "_" not in display: # check if it has underscored in the display variable, which means that the user wins the game
        game_over = True # change boolean value of the variable to leave the while looping
        print("****************************YOU WIN****************************")


    print(stages[lives]) #print the hangman accordingly users progress
