print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage would you like to tip?" ))
people = int(input("How many people are gonna split the bill? "))

bill_per_person = (bill + tip) / people

total_amount = round(bill_per_person,2)
final_amount =  "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")