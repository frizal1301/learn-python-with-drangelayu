# rock - paper - scissor
import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# choice = [rock, paper, scissors]

random_number = random.randint(0, 2)

input_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if input_choice < 0 or input_choice > 2 : 
    print("You typed an invalid number! You Lose")

if input_choice == 0 :
    user_choice = rock 
elif input_choice == 1 :
    user_choice = paper
elif input_choice == 2 :
    user_choice = scissors

print(user_choice)

if random_number == 0 :
    computer_choice = rock
elif random_number == 1 :
    computer_choice = paper
else :
    computer_choice = scissors

print(f"Computer chose: \n{computer_choice}")

# aturan
# rock(batu)    vs paper(kertas)    -> paper
# rock(batu)    vs scissor(gunting) -> rock
# paper(kertas) vs scissor(gunting) -> scissor

# user_choice -> rock
if user_choice == rock and computer_choice == paper :
    print("You lose")
elif user_choice == rock and computer_choice == scissors :
    print("You win")

# user_choice -> scissor
elif user_choice == scissors and computer_choice == paper :
    print("You win")
elif user_choice == scissors and computer_choice == rock :
    print("You lose")

# user_choice -> paper
elif user_choice == paper and computer_choice == rock :
    print("You win")
elif user_choice == paper and computer_choice == scissors :
    print("You lose")

# draw
elif user_choice == computer_choice :
    print("It's draw")






