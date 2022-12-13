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


# function to return itemID in item_list
def Extract(lists):
    return [thing[0] for thing in lists]


# ----PART 1------
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
    # separates the dates by '/'
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
            # sort by the price from most to least expensive
            item_list.sort(key=sortPrice, reverse=True)
            # format
            damaged_file.write(f'{row[0]},{row[1]},{row[3]},{row[4]},{row[5]}\n')

# -----PART 2-----
# creates new list for users
user_list = []
for row in item_list:
    # only adds items that aren't damaged and has not pass the due date
    if row[5] != 'damaged':
        user_list.append(row)
        today = datetime.date.today()
        date_separate = row[4].split('/')
        serve_date = datetime.date(int(date_separate[2]), int(date_separate[0]), int(date_separate[1]))
        # finds difference btw date and current date
        time_difference = serve_date - today
        if time_difference.days < 0:
            user_list.remove(row)
    # sorts prices from most to least expensive
    user_list.sort(key=sortPrice, reverse=True)
while True:
    user_input = input('Please enter the manufacturer and item type:\n').split()
    manufacturer_item_list = []
    # filters if user_input has more than 2 words to get rid of extra words
    if len(user_input) > 2:
        manufacturer_item_list.append(user_input[len(user_input) - 2])
        manufacturer_item_list.append(user_input[len(user_input) - 1])
    elif len(user_input) == 2:
        # if user_input has 2 words
        manufacturer_item_list = user_input
    # allows user to quit when input is q
    elif len(user_input) == 1 and 'q':
        break
    else:
        print("Please enter again")
    success = False
    for product in user_list:
        # prints out match that user is looking for
        if manufacturer_item_list[0] in product[1] and manufacturer_item_list[1] in product[2]:
            print('Your item is:', f'{product[0]}, {product[1]}, {product[2]}, ${product[3]}')
            # item is found
            success = True
            # finds same item with similar price
            similar_success = False
            for similar_product in user_list:
                if manufacturer_item_list[0] not in similar_product[1] and manufacturer_item_list[1] in similar_product[2]:
                    print("You may, also, consider:",
                          f'{similar_product[0]}, {similar_product[1]}, {similar_product[2]}, ${similar_product[3]}')
                    similar_success = True
            if not similar_success:
                print("There are no other similar items")
    # prints out that user_input entered could not be found in inventory
    if not success:
        print("No such item in inventory")