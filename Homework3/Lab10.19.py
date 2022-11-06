# JenniferChu
# 1873159

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none') -> object:
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@', f'${self.item_price}',
              '= ${}'.format(self.item_quantity * self.item_price))

    def print_item_description(self):
        print(self.item_name + ":" + self.item_description)


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, more_items):
        self.cart_items.append(more_items)

    def remove_item(self, item_name):
        if item_name in self.cart_items:
            del self.cart_items[item_name]
        else:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item: ItemToPurchase):
        count = 0
        items = self.cart_items[:]
        for i in range(len(items)):
            item = items[i]
            if item.item_name == ItemToPurchase.item_name:
                count += 1



    def get_num_items_in_cart(self):
        count = 0
        items = self.cart_items[:]
        for i in range(len(items)):
            item1 = items[i]
            count += item1.item_quantity
        return count

    def get_cost_of_cart(self):
        cost = 0
        items = self.cart_items[:]
        for i in range(len(items)):
            item = items[i]
            cost += (item.item_quantity * item.item_price)
        return cost

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("Item Descriptions")
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            for i in self.cart_items:
                print(i.item_name + ": " + i.description)

    def print_total(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        count = len(self.cart_items)
        print("Number of Items: " + str(count) + "\n")
        total = self.cart_items
        if count == 0:
            print('SHOPPING CART IS EMPTY\n')
            print("Total: $0")
        else:
            print("Total: $" + str(total))

def menu():
    print("\nMENU")
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit\n")


if __name__ == "__main__":
   cust_name = input("Enter customer's name:\n")
   today_date = input("Enter today's date:\n")
   print("\nCustomer name:", cust_name)
   print("Today's date:", today_date)
   shop = ShoppingCart(cust_name, today_date)

   while True:
       menu()
       option = input("Choose an option:\n")
       if option == 'a':
           print("ADD ITEM TO CART")
           item_name = input("Enter the item name:\n")
           description = input("Enter the item description:\n")
           price = int(input("Enter the item price:\n"))
           quantity = int(input("Enter the item quantity:\n"))
           sale = ItemToPurchase(item_name, description, price, quantity)
           shop.add_item(sale)
       elif option == 'r':
           print("REMOVE ITEM FROM CART")
           remove_item = input("Enter name of item to remove:\n")
           shop.remove_item(remove_item)
       elif option == 'c':
           print("CHANGE ITEM QUANTITY")
           item_name = input("Enter the item name:\n")
           quantity = input("Enter the new quantity:\n")
           change_quantity = ItemToPurchase(item_name)
           change_quantity.item_quantity(quantity)
           shop.modify_item(change_quantity)
       elif option == 'i':
           shop.print_total()
       elif option == 'o':
           print("OUTPUT SHOPPING CART")
           shop.print_total()
       elif option == 'q':
           break
       elif option != 'a' or 'r' or 'c' or 'i' or 'q':
           input("Choose an option:\n")
           option = input("Choose an option:\n")