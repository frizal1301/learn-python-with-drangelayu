# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total = 0
number_of_students = 0

for height in student_heights :
    total += height
    number_of_students += 1

average = total / number_of_students

print(f"total height = {total}")
print(f"number of students = {number_of_students}")
print(f"average height = {round(average)}")