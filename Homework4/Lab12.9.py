# JenniferChu
# 1873159

name_age = input().split()
name = name_age[0]

while name != '-1':
    try:
        age = int(name_age[1]) + 1
        print("{} {}".format(name, age))
        name_age = input().split()
        name = name_age[0]
    except ValueError:
        age = 0
        print("{} {}".format(name, age))
        name_age = input().split()
        name = name_age[0]
