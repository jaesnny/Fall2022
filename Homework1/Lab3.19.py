# JenniferChu
# 1873159

import math
wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))
wall_area = wall_width * wall_height
print("Wall area:", wall_area, "square feet")
paint_gallon = wall_area / 350
print("Paint needed:", f'{paint_gallon:.2f}', "gallons")
cans = math.ceil(paint_gallon)
print("Cans needed:", cans, "can(s)\n")
color = input("Choose a color to paint the wall:\n")
if color == "red":
    red_paint = cans * 35
    print("Cost of purchasing red paint:",f'${red_paint:.0f}')
elif color == "blue":
    blue_paint = cans * 25
    print("Cost of purchasing blue paint:",f'${blue_paint:.0f}')
else:
    green_paint = cans * 23
    print("Cost of purchasing green paint:",f'${green_paint:.0f}')
