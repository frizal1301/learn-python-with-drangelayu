# Welcome to the tip calculator.
# What was the total bill ? $
# What percentage tip would you like to give ? 10, 12, or 15?
# How many people to split the bill?
# Each person should pay
print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

billWithTip = bill * tip / 100 + bill

tipAsPercent = tip / 100
totalTipAmount = bill * tipAsPercent
totalBill = bill + totalTipAmount

billPerPerson = round(totalBill / people, 2)


print(f"Each person should pay: ${billPerPerson}")