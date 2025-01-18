import random

names_string = input("Write everyone's name.\n Kindly use commas.")
names = names_string.split(",")


person_who_will_pay = random.choice(names)

print(person_who_will_pay + " is going to buy the meal today.")