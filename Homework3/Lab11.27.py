# JenniferChu
# 1873159


roster = {}
for i in range(0, 5):
    jersey = int(input("Enter player %s's jersey number:\n" % str(i + 1)))
    if jersey not in range(0, 100):
        print("Not a jersey number")
    rating = int(input("Enter player %s's rating:\n" % str(i + 1)))
    if rating not in range(0, 10):
        print("Not a valid rating")
    if jersey not in roster:
        roster[jersey] = rating
    print()

print("ROSTER")
for j, r in sorted(roster.items()):
    print("Jersey number: %d, Rating: %d" % (j, r))

menu = {}
while True:
    print('\nMENU')
    menu['a'] = 'Add player'
    menu['d'] = 'Remove player'
    menu['u'] = 'Update player rating'
    menu['r'] = 'Output players above a rating'
    menu['o'] = 'Output roster'
    menu['q'] = 'Quit'
    for options, actions in menu.items():
        print("%s - %s" % (options, actions))

    choice = input('\nChoose an option:\n')
    if choice.lower() == 'a':
        jersey = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        if jersey not in roster:
            roster[jersey] = rating
        else:
            print("This player is already in the roster")
    elif choice.lower() == 'd':
        jersey = int(input("Enter a jersey number:\n"))
        if jersey in roster:
            del roster[jersey]
        else:
            print("This player is not in the roster")
    elif choice.lower() == 'u':
        jersey = int(input("Enter a jersey number: "))
        if jersey in roster:
            rating = int(input("Enter a new rating for player: "))
            roster[jersey] = rating
        else:
            print("This player is not in the roster.\n")
    elif choice.lower() == 'r':
        rating = int(input("Enter a rating:\n"))
        print("ABOVE", rating)
        for j, r in sorted(roster.items()):
            if r > rating:
                print("Jersey number: %d, Rating: %d" % (j, r))
    elif choice.lower() == 'o':
        print("ROSTER")
        for j, r in sorted(roster.items()):
            print("Jersey number: %d, Rating: %d" % (j, r))
    elif choice.lower() == 'q':
        break
    else:
        print("Not a valid option, please try again")
