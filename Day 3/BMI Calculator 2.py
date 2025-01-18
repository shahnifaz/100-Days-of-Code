height = float(input("Enter your height in metre : "))
weight = float(input("Enter your weight in kilogram : "))

bmi = round(weight / height ** 2)

if  bmi < 18.5:
    print(f"You BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"You BMI is {bmi}, you have a normal weight.")
elif  bmi < 30:
    print(f"You BMI is {bmi}, you are overweight.")
elif  bmi < 35:
    print(f"You BMI is {bmi}, you are obese.")
else:
    print(f"You BMI is {bmi}, you are severely obese.")

