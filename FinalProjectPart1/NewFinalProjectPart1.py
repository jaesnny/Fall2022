# Jennifer Chu
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


# function to access itemID in item_list
def Extract(lists):
    return [thing[0] for thing in lists]


# part a
item_list = []

# takes ManufacturerList.csv as input
manufacturer_list = csv.reader(open('ManufacturerList.csv'), delimiter=',')
# takes PriceList.csv as input
price_list = csv.reader(open("PriceList.csv"), delimiter=',')
# takes ServiceDateList.csv as input
service_dates_list = csv.reader(open("ServiceDatesList.csv"), delimiter=',')

with open('FinalProjectFullInventory.csv', 'w') as full_inventory_file:
    # sort alphabetically by manufacturer
    for item in manufacturer_list:
        item_list.append(item)
        item_list.sort(key=sortMan)
    # appends price_list and service_dates_list into item_list
    for price in price_list:
        price_index = Extract(item_list).index(price[0])
        for i in range(0, len(Extract(item_list))):
            if price_index == i:
                item_list[i].insert(3, price[1])
    for day in service_dates_list:
        date_index = Extract(item_list).index(day[0])
        for i in range(0, len(Extract(item_list))):
            if date_index == i:
                item_list[i].insert(4, day[1])
    for row in item_list:
        # format
        full_inventory_file.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}\n")

# part b
# writes new files for laptops
with open('FinalProjectLaptop.csv', 'w') as laptop_file:
    for row in item_list:
        # sort by itemID
        item_list.sort(key=sortID)
        if row[2] == 'laptop':
            # format
            laptop_file.write(f"{row[0]},{row[1]},{row[3]},{row[4]},{row[5]}\n")

# writes new files for phones
with open('FinalProjectPhone.csv', 'w') as phone_file:
    for row in item_list:
        # sort by itemID
        item_list.sort(key=sortID)
        if row[2] == 'phone':
            # format
            phone_file.write(f"{row[0]},{row[1]},{row[3]},{row[4]},{row[5]}\n")

# writes new files for towers
with open('FinalProjectTower.csv', 'w') as tower_file:
    for row in item_list:
        # sort by itemID
        item_list.sort(key=sortID)
        if row[2] == 'tower':
            # format
            tower_file.write(f"{row[0]},{row[1]},{row[3]},{row[4]},{row[5]}\n")

# part c
# finds dates that are past current date
with open("FinalProjectPastServiceDate.csv", 'w') as past_service_date_file:
    # get current date
    today = datetime.date.today()
    # seperates the dates by '/'
    for row in item_list:
        date_separate = row[4].split('/')
        serve_date = datetime.date(int(date_separate[2]), int(date_separate[0]), int(date_separate[1]))
        # finds difference btw date and current date
        time_difference = serve_date - today
        if time_difference.days < 0:
            # sorts date
            item_list.sort(key=sortDate)
            # format
            past_service_date_file.write(f'{row[0]},{row[1]},{row[3]},{row[4]},{row[5]}\n')

# part d
with open('FinalProjectDamaged.csv', 'w') as damaged_file:
    for row in item_list:
        # filters out for only items that are damaged
        if row[5] == 'damaged':
            # sort by the price from least to most expensive
            item_list.sort(key=sortPrice, reverse=True)
            # format
            damaged_file.write(f'{row[0]},{row[1]},{row[3]},{row[4]},{row[5]}\n')
