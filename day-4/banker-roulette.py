names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random 

num_items = len(names)

random_items = random.randint(0, num_items - 1)

print(f"{names[random_items]} is going to buy the meal today!")
