############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start_play = input("Do you want to play a game of Blackjack, Type 'y' or 'n':")

def calculate_score(list_card) :
    return sum(list_card)

def add_card(cards) :
    cards.append(random.choice(cards))

def show_cards(user_cards, computer_cards) :
    print(f"    Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"    Computer's first card: {computer_cards[0]}")

def compare(user_score, computer_score) :
    if user_score > 21 :
        return "You went over. You lose"
    elif computer_score > 21 :
        return "Opponent went over. You win!" 
    elif user_score == computer_score :
        return "Draw"
    elif user_score > 21 and computer_score <= 21 :
        print("You lose ")
    elif computer_score == 21 :
        print("You lose")
    elif user_score == 21 and computer_score < 21 :
        print("You win")
    elif user_score > computer_score :
        print("You win")
    elif user_score < computer_score :
        print("You lose")

if start_play == 'y' :
    game_over = False
    while not game_over :

        print(logo)

        user_cards = []
        computer_cards = []

        for _ in range(2) :
            add_card(user_cards)
            add_card(computer_cards)
        
        show_cards(user_cards, computer_cards)

        while calculate_score(computer_cards) <= 16 :
            add_card(computer_cards)

        another_card = True

        while another_card :
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if get_another_card == 'y' :
                add_card(user_cards)
    
                if calculate_score(user_cards) > 21 :
                    another_card = False

                show_cards(user_cards, computer_cards)
            else :
                another_card = False

        if calculate_score(user_cards) > 21 and 11 in user_cards :
            user_cards[user_cards.index(11)] = 1
        elif calculate_score(computer_cards) > 21 and 11 in computer_cards :
            computer_cards[computer_cards.index(11)] = 1

        show_cards(user_cards, computer_cards)

        print(f"  Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
        print(f"  Computer's final hand: {computer_cards} final score: {calculate_score(computer_cards)}")

        print(compare(calculate_score(user_cards), calculate_score(computer_cards)))
        
        continue_game = input("\nDo you want to play a game of blackjack? type 'y' or 'n': ");

        if continue_game == 'n' :
            game_over = True

