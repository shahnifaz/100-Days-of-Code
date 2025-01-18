height = input("Enter your height in metre : ")
weight = input("Enter your weight in kilogram : ")

bmi = (float(weight) / float(height) ** 2)
print(round(bmi, 2))