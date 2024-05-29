line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = "B3" # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].lower()
# mengubah format huruf dari inputan menjadi index misalkan B1, B diubah menjadi format index dalam hal ini 1
abc = ["a", "b", "c"]

letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
  
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")










# cara tidak efisien
# if position == "A1" :
#   map[0][0] = "X"
# elif position == "A2" :
#   map[1][0] = "X"
# elif position == "A3" :
#   map[2][0] = "X"
# elif position == "B1" :
#   map[0][1] = "X"
# elif position == "B2" :
#   map[1][1] = "X"
# elif position == "B3" :
#   map[2][1] = "X"
# elif position == "C1" :
#   map[0][2] = "X"
# elif position == "C2" :
#   map[1][2] = "X"
# elif position == "C3" :
#   map[2][2] = "X"

