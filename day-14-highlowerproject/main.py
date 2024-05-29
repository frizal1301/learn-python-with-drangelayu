from art import logo, vs
from game_data import data
from replit import clear
import random

def check_has_more_follower(answer, data1, data2) :
    if data1 > data2 :
        return answer == "a"
    else :
        return answer == "b"

def format_data(data) :
    name = data['name']
    description = data['description']
    country = data['country']

    return f"{name}, a {description}, from {country}"

def get_random_value():
    return random.choice(data)

def game() :
    print(logo)
    
    score = 0
    data1 = get_random_value()
    data2 = get_random_value()

    game_should_continue = True

    while game_should_continue :
        while data1 == data2 :
            data2 = get_random_value()

        print(f"Compare A: {format_data(data1)}.")
        print(vs)
        print(f"Against B: {format_data(data2)}.")
    
        guess = input("Who has more followers. Type 'A' or 'B': ")

        data1_follower_count = data1["follower_count"]
        data2_follower_count = data2["follower_count"]

        check_answer = check_has_more_follower(guess, data1_follower_count, data2_follower_count)

        if check_answer :
            score += 1
            print(f"You're right! Current score: {score}.")
        else :
            print(f"Sorry that's wrong. Final score: {score}")
            print(logo)
            game_should_continue = False

        data1 = data2
        data2 = get_random_value()
game()