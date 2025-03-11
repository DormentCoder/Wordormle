import random #1-3: the imported functions
import time
import sys

# Function to select a random word of the specified length from the words_list
def select_random_word4():
    with open('words.txt') as f: #as the text file is being read by the program
        words = f.read().splitlines() 
        return random.choice(words) #this returns a randomly selected word to the function

# Function to select a random word of the specified length from the words_list
def select_random_word5():
    with open('words2.txt') as f: #as the text file is being read by the program
        words = f.read().splitlines() 
        return random.choice(words) #this returns a randomly selected word to the function
    
# Function to select a random word of the specified length from the words_list
def select_random_word6():
    with open('words3.txt') as f: #as the text file is being read by the program
        words = f.read().splitlines() 
        return random.choice(words) #this returns a randomly selected word to the function

# Function to handle the player's decision to give up
def give_up4():
    print('The correct word is', word4) #this prints when the give_up function is called
    
# Function to handle the player's decision to give up
def give_up5():
    print('The correct word is', word5) #this prints when the give_up function is called
    
# Function to handle the player's decision to give up
def give_up6():
    print('The correct word is', word6) #this prints when the give_up function is called

#main game loop
def main4():
    print('Wordormle (4 character word)')
    print('Guess: \n') #45-46: User Interface for game 
    def display_result():   
        print('') 
        print('You have successfully guessed the Wordormle!') #56-58: prints to the user that they have figured it out and that they have completed it in i amount of tries
        print('You have guessed it in', {guess_attempt}, 'attempts.')
    for guess_attempt in range(1, 7): #gives the user 6 attempts to figure out the wordle
        guess = input().lower() #makes all inputs automatically into lower case
        sys.stdout.write('\x1b[1A') #47-48: these are 2 lines of code running alongside the sys import that is designed to show the outputted result while removing the result prior from the terminal
        sys.stdout.write('\x1b[2K')
        for i in range(min(len(guess), 4)): #makes sure that the user input is within 5 words or close to 5 characters as possible at all times
            if i < len(guess) and guess[i] == word4[i]: #if the user input can be read by the program, then lines 51-58 can be run onwards
                print(guess[i], '*', end='') #this line shows an asterisk character if the letter is in the correct spot
            elif guess[i] in word4: #if the character is somewhere within the word but is in the wrong space...
                print(guess[i], '+', end='') #...then show the user the + symbol
            elif guess == 'endgame': #if the user types in 'endgame'...
                give_up4() #...then the giveup function is called
            else: #if all goes wrong...
                print(guess[i], '_', end='') #...show the user the underscore symbol
        if guess == word4: #if the guess is directly the word...
            display_result()   #then the result is shown to the user...
            restart = (input('Want to play again? (no = quit) ')) #and the user is asked if they want to play again...
            while restart != 'no': #and as long as the input isnt 'no', then it will continuously loop
                main4() 
        while guess_attempt in range(1, 7): #19-22: timer function
            counter = 0
            time.sleep(1)
            counter = counter + 1
            if counter > 30: #if 30 seconds has passed...
                print('Times Up!')
                sys.exit() #end the game

#main game loop
def main5():
    print('Wordormle (5 character word)')
    print('Guess: \n') #45-46: User Interface for game 
    def display_result():   
        print('') 
        print('You have successfully guessed the Wordormle!') #56-58: prints to the user that they have figured it out and that they have completed it in i amount of tries
        print('You have guessed it in', {guess_attempt}, 'attempts.')
    for guess_attempt in range(1, 7): #gives the user 6 attempts to figure out the wordle
        guess = input().lower() #makes all inputs automatically into lower case
        sys.stdout.write('\x1b[1A') #47-48: these are 2 lines of code running alongside the sys import that is designed to show the outputted result while removing the result prior from the terminal
        sys.stdout.write('\x1b[2K')
        for i in range(min(len(guess), 5)): #makes sure that the user input is within 5 words or close to 5 characters as possible at all times
            if i < len(guess) and guess[i] == word5[i]: #if the user input can be read by the program, then lines 51-58 can be run onwards
                print(guess[i], '*', end='') #this line shows an asterisk character if the letter is in the correct spot
            elif guess[i] in word5: #if the character is somewhere within the word but is in the wrong space...
                print(guess[i], '+', end='') #...then show the user the + symbol
            elif guess == 'endgame': #if the user types in 'endgame'...
                give_up5() #...then the giveup function is called
            else: #if all goes wrong...
                print(guess[i], '_', end='') #...show the user the underscore symbol
        if guess == word5: #if the guess is directly the word...
            display_result()   #then the result is shown to the user...
            restart = (input('Want to play again? (no = quit) ')) #and the user is asked if they want to play again...
            while restart != 'no': #and as long as the input isnt 'no', then it will continuously loop
                main5() 
        while guess_attempt in range(1, 7): #19-22: timer function
            counter = 0
            time.sleep(1)
            counter = counter + 1
            if counter > 30: #if 30 seconds has passed...
                print('Times Up!')
                sys.exit() #end the game
                
#main game loop
def main6():
    print('Wordormle (6 character word)')
    print('Guess: \n') #45-46: User Interface for game 
    def display_result():   
        print('') 
        print('You have successfully guessed the Wordormle!') #56-58: prints to the user that they have figured it out and that they have completed it in i amount of tries
        print('You have guessed it in', {guess_attempt}, 'attempts.')
    for guess_attempt in range(1, 7): #gives the user 6 attempts to figure out the wordle
        guess = input().lower() #makes all inputs automatically into lower case
        sys.stdout.write('\x1b[1A') #47-48: these are 2 lines of code running alongside the sys import that is designed to show the outputted result while removing the result prior from the terminal
        sys.stdout.write('\x1b[2K')
        for i in range(min(len(guess), 6)): #makes sure that the user input is within 5 words or close to 5 characters as possible at all times
            if i < len(guess) and guess[i] == word6[i]: #if the user input can be read by the program, then lines 51-58 can be run onwards
                print(guess[i], '*', end='') #this line shows an asterisk character if the letter is in the correct spot
            elif guess[i] in word6: #if the character is somewhere within the word but is in the wrong space...
                print(guess[i], '+', end='') #...then show the user the + symbol
            elif guess == 'endgame': #if the user types in 'endgame'...
                give_up6() #...then the giveup function is called
            else: #if all goes wrong...
                print(guess[i], '_', end='') #...show the user the underscore symbol
        if guess == word6: #if the guess is directly the word...
            display_result()   #then the result is shown to the user...
            restart = (input('Want to play again? (no = quit) ')) #and the user is asked if they want to play again...
            while restart != 'no': #and as long as the input isnt 'no', then it will continuously loop
                main6() 
        while guess_attempt in range(1, 7): #19-22: timer function
            counter = 0
            time.sleep(1)
            counter = counter + 1
            if counter > 30: #if 30 seconds has passed...
                print('Times Up!')
                sys.exit() #end the game

word4 = select_random_word4()
word5 = select_random_word5() #this line makes the program pick a word at random
word6 = select_random_word6()
print('Welcome to Wordormle.')
game_choice = input('Pick a difficulty. easy/medium/hard: ')
if game_choice == 'easy':
    main4()
elif game_choice == 'medium':
    main5()
elif game_choice == 'hard':
    main6()
else:
    print('Unregistered input.')
    print('Please restart the program to try again.')