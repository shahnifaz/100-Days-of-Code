print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage would you like to tip? "))
people = int(input("How many people are gonna split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = round(bill * tip_as_percent, 2)

total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Total tip amount: ${total_tip_amount}")
print(f"Total bill amount: ${total_bill}")
print(f"Each person should pay: ${final_amount}")