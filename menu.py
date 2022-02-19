"""Part of code that reproduce a interactive LogicSystem control """
from order import Order, used_orderid
from location import Location
from item import Item
from vehicle import Vehicle, station
from logicsystem import LogisticSystem
import sys


class Menu:
    def __init__(self):
        """Show a menu and respond a choice, when it run"""
        self.orders = LogisticSystem(station)
        self.choices = {
            '1': self.add_order,
            '2': self.trackorder,
            '3': self.add_vehicle,
            '4': self.show_transport,
            '5': self.show_orders,
            '6': self.quit
        }

    def display_menu(self):
        print("""
        1. Create a new order
        2. Track order
        3. Add a new vehicle(transport)
        4. View transports
        5. View orders
        6. Quit
        """)

    def run(self):
        """Displays the menu a and repsonds to choices"""
        while True:
            self.display_menu()
            choise = input('Enter an option: ')
            action = self.choices.get(choise)
            if action:
                action()
            else:
                print(f'{choise} is not a valid')

    def show_transport(self):
        for transport in station:
            print(transport)
            print('-------------------')

    def show_orders(self):
        for order in self.orders.orders:
            print(order)
            print("===================")

    def add_vehicle(self):
        name = False
        while not name:
            name = input('Enter a name: ')
        print(f'Your transport({name}) has been added')
        Vehicle(name)

    def add_order(self):
        user_name = input('Enter a name: ')
        city = input('Enter a city: ')
        post_office = input('Enter a post office: ')
        items = []
        items_const = False
        while not items_const:
            item_name = input('Enter the product name: ')
            item_price = input('Enter the product price: ')
            if not item_price.isdigit():
                correct_write = False
                try:
                    for elements in item_price.split('.'):
                        if elements.isdigit():
                            continue
                        else:
                            correct_write = True
                            break
                except:
                    print('The price must be a number')
                    while not item_price.isdigit() and correct_write:
                        item_price = input('Enter correct product price: ')
            item = Item(item_name, item_price)
            items.append(item)
            print('_______________________________________________________')
            next_action = input('If you want continue add items, print "add".\n'
                                'If you have already added all the things, print "stop": ')
            if next_action == 'stop':
                items_const = True
            print('_______________________________________________________')
        orderId = input('Enter the order number: ')
        if orderId == '':
            current_order = Order(user_name=user_name, city=city, postoffice=post_office, items=items)
        else:
            current_order = Order(user_name=user_name, city=city, postoffice=post_office, items=items, orderId=orderId)
        print(current_order)
        if current_order.vehicle.vehicleNo == False:
            print('We don`t have free vehicle. Add a new vehicle.')
        else:
            actions = ''
            while actions != 'N' and actions != 'Y':
                actions = input('Do you want to send your order (Y/N): ')
            if actions == 'N':
                print('Your order has been deleted')
            if actions == 'Y':
                self.orders.placeOrder(current_order)

    def trackorder(self):
        trackid = input('Enter the order id: ')
        self.orders.trackOrder(trackid)

    def quit(self):
        print('Thank you for working with Logistic System today')
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
