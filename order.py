"""Class for working with Logic System"""
from location import Location
from item import Item
from vehicle import Vehicle, station

used_orderid = set('0')


class Order:
    """Contains all information about order and user"""
    def assignVehicle(self):
        for auto in station:
            if auto.isAvailable == True:
                result = auto
                auto.isAvailable = self.location
                return result
        return False

    def seperate_items(self, items):
        diliver_items = ''
        for elements in items:
            diliver_items = diliver_items + elements.name + ', '
        diliver_items = diliver_items[:-2]
        return diliver_items

    def diliver_price(self, items):
        diliver_price = 0
        for elements in items:
            diliver_price += float(elements.price)
        return diliver_price

    def __init__(self, user_name: str, city: str, postoffice: str, items: list, orderId=''):
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = self.seperate_items(items)
        self.price = self.diliver_price(items)
        self.vehicle = self.assignVehicle()
        global used_orderid
        if orderId == '':
            for id in used_orderid:
                start_point = int(id)
                if str(start_point + 1) in used_orderid:
                    continue
                else:
                    self.orderId = str(start_point + 1)
                    used_orderid.add(str(start_point + 1))
                    break
        else:
            if str(orderId).isdigit():
                if orderId not in used_orderid:
                    self.orderId = orderId
                    used_orderid.add(orderId)
                else:
                    for id in used_orderid:
                        start_point = int(id)
                        if str(start_point + 1) in used_orderid:
                            continue
                        else:
                            self.orderId = str(start_point + 1)
                            used_orderid.add(str(start_point + 1))
                            break
            else:
                for id in used_orderid:
                    start_point = int(id)
                    if str(start_point + 1) in used_orderid:
                        continue
                    else:
                        self.orderId = str(start_point + 1)
                        used_orderid.add(str(start_point + 1))
                        break
        print(f'Your order number is {self.orderId}')

    def __str__(self):
        return f'order id: {self.orderId}\n' \
               f'customer name: {self.user_name}\n' \
               f'location: {self.location}\n' \
               f'items: {self.items}\n' \
               f'price: {self.price} UAH\n' \
               f'vehicle: {self.vehicle}'

    def __repr__(self):
        return f'order id: {self.orderId}\n' \
               f'customer name: {self.user_name}\n' \
               f'location: {self.location}\n' \
               f'items: {self.items}\n' \
               f'price: {self.price} UAH\n' \
               f'vehicle: {self.vehicle}'

    def calculateAmount(self):
        try:
            return self.price
        except:
            total_price = 0
            for item in self.items:
                total_price += float(item.price)
            return total_price
