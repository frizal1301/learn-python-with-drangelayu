#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from random import randint

EASY_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 10

def compare_guess(guess, actual_answer) :
    if guess > actual_answer :
        return "Too High."
    elif guess < actual_answer :
        return "Too Low."
    else :
        return f"You got it! The answer was {actual_answer}."

def set_difficulty() :
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

    if difficulty == 'easy' :
        return EASY_LEVEL_TURNS
    else :
        return HARD_LEVEL_TURNS 

def game() :
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number beetween 1 of 100.")

    actual_answer = randint(1,100)
    print(f"Psst, the correct answer is {actual_answer}")

    number_of_attempts = set_difficulty()
    
    guess = 0
    while guess != actual_answer :  
        print(f"You have {number_of_attempts} remaining to guess the number")
        guess = int(input("Make a guess: "))

        print(compare_guess(guess, actual_answer))

        number_of_attempts -= 1  
        
        if number_of_attempts == 0 :
            print("You've run out of guesses. You lose!")
            return

        print("Guess Again")
game()


