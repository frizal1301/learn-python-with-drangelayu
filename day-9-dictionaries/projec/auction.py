from replit import clear
from art import logo

print(logo)

print("Welcome to the secret auction program.")

bidders = {}

end = False 

def find_highest_bidder(biddest_record) :
    highest_bid = 0

    for bidder in biddest_record :
        if biddest_record[bidder] > highest_bid :
            highest_bid = biddest_record[bidder]
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not end :
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if should_continue == "no" :
        end = True
        find_highest_bidder(bidders)
    else :
        clear()    



