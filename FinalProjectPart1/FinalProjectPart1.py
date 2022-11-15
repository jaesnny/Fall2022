# JenniferChu
# 1873159

import csv
import datetime


# function to sort by manufacturers
def sortMan(col):
    return col[1]


# function to sort by item ID
def sortID(col):
    return col[0]


# function to sort by date
def sortDate(col):
    split_date = col[4].split('/')
    return split_date[2], split_date[0]


# function to sort by price
def sortPrice(col):
    return col[3]


# part a
item_list = []

full_inventory = csv.reader(open('FullInventory.csv'), delimiter=',')
with open('FinalProjectFullInventory.csv', 'w') as full_inventory_file:
    # sort alphabetically by manufacturer
    for element in full_inventory:
        item_list.append(element)
        item_list.sort(key=sortMan)
    # format
    for row in item_list:
        full_inventory_file.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}\n")

# part b
# writes new file for phones
with open('FinalProjectPhone.csv', 'w') as phone_file:
    for row in item_list:
        # sort by itemID
        item_list.sort(key=sortID)
        # looks for phones only
        if row[2] == 'phone':
            # format
            phone_file.write(f"{row[0]},{row[1]},{row[3]},{row[4]},{row[5]}\n")
# writes new files for laptops
with open('FinalProjectLaptop.csv', 'w') as laptop_file:
    for row in item_list:
        # sort by itemID
        item_list.sort(key=sortID)
        # looks for laptops only
        if row[2] == 'laptop':
            # format
            laptop_file.write(f"{row[0]},{row[1]},{row[3]},{row[4]},{row[5]}\n")
with open("FinalProjectTower.csv", 'w') as tower_file:
    for row in item_list:
        # sort by itemID
        item_list.sort(key=sortID)
        # looks for towers only
        if row[2] == 'tower':
            # format
            tower_file.write(f"{row[0]},{row[1]},{row[3]},{row[4]},{row[5]}\n")

# part c
with open('FinalProjectPastServiceDate.csv', 'w') as past_service_file:
    # current date
    today_date = datetime.date.today()
    for row in item_list:
        # splits date by /
        date_sep = row[4].split('/')
        # reformat date to today_date
        serve_date = datetime.date(int(date_sep[2]), int(date_sep[0]), int(date_sep[1]))
        # gets time difference between current date and service date
        time_difference = serve_date - today_date
        # if days are less than 0 then service date has passed
        if time_difference.days < 0:
            # sort by dates
            item_list.sort(key=sortDate)
            # format
            past_service_file.write(f"{row[0]},{row[1]},{row[3]},{row[4]},{row[5]}")

# part d
with open('FinalProjectDamaged.csv', 'w') as damaged_file:
    for row in item_list:
        # sorts prices by most expensive to least expensive
        item_list.sort(key=sortPrice, reverse=True)
        # filters out for only damaged items
        if row[5] == 'damaged':
            damaged_file.write(f"{row[0]},{row[1]},{row[3]},{row[4]},{row[5]}\n")