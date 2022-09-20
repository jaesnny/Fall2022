#JenniferChu
#1873159

#Part1
lemon = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
lemonade = float(input("How many servings does this make?\n"))

print("\nLemonade ingredients - yields", f'{lemonade:.2f}'.format(lemonade), "servings")
print(f'{lemon:.2f}'.format(lemon),"cup(s) lemon juice")
print(f'{water:.2f}'.format(water),"cup(s) water")
print(f'{agave:.2f}'.format(agave),"cup(s) agave nectar\n")

#Part2
servings = float(input("How many servings would you like to make?\n"))
print("\nLemonade ingredients - yields", f'{servings:.2f}'.format(servings), "servings")
lemon_one = lemon / lemonade
lemon_servings = lemon_one * servings
print(f'{lemon_servings:.2f}'.format(lemon_servings), "cup(s) lemon juice")
water_one = water / lemonade
water_servings = water_one * servings
print(f'{water_servings:.2f}'.format(water_servings), "cup(s) water")
agave_one = agave / lemonade
agave_servings = agave_one * servings
print(f'{agave_servings:.2f}'.format(agave_servings), "cup(s) agave nectar\n")

#Part3
print("Lemonade ingredients - yields", f'{servings:.2f}'.format(servings),"servings")
lemon_gallon = lemon_servings / 16
print(f'{lemon_gallon:.2f}'.format(lemon_gallon),"gallon(s) lemon juice")
water_gallon = water_servings / 16
print(f'{water_gallon:.2f}'.format(water_gallon), "gallon(s) water")
agave_gallon = agave_servings / 16
print(f'{agave_gallon:.2f}'.format(agave_gallon),"gallon(s) agave nectar")