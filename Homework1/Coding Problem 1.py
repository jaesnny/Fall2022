#JenniferChu
#1873159

age = 0
print("Birthday Calculator")
print("Current day")
current_month = int(input("Month: "))
current_day = int(input("Day: "))
current_year = int(input("Year: "))
print("Birthday")
birth_month = int(input("Month: "))
birth_day = int(input("Day: "))
birth_year = int(input("Year: "))
if current_month > birth_month:
    age = current_year - birth_year
elif current_month < birth_month:
    age = current_year - birth_year - 1
elif current_month == birth_month:
    if current_day > birth_day:
        age = current_year - birth_year
    elif current_day < birth_day:
        age = current_year - birth_year - 1
    elif current_day == birth_day:
        print("Happy birthday!")
        age = current_year - birth_year
print("You are", age, "years old.")