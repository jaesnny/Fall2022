#JenniferChu
#1873159

class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0) -> object:
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@', f'${self.item_price}', '= ${}'.format(self.item_quantity * self.item_price))

if __name__ == "__main__":
    item1 = ItemToPurchase()
    print('Item 1')
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input('Enter the item quantity:\n'))


    item2 = ItemToPurchase()
    print('\nItem 2')
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    item_total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print("\nTotal:", f'${item_total}')