import math

def  paint_calc(height, width, cover):
   area = height * width
   num_of_cans = math.ceil(area / cover)
   print(f"You'll need {num_of_cans} cans of paint.")

h = int(input("height_of_wall : "))
w = int(input("width_of_wall : "))
coverage = 5

paint_calc(height = h, width = w, cover = coverage)

