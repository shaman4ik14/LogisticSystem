"""My program"""
from order import Order, used_orderid
from location import Location
from item import Item
from vehicle import Vehicle, station


class LogisticSystem:
    """Main class that contains all information: usernames, orders, transports"""
    def __init__(self, vehicles: list):
        self.orders = []
        self.vehicles = station
        vehicles

    def placeOrder(self, order: Order):
        self.orders.append(order)

    def trackOrder(self, orderId):
        announcement = False
        for order in self.orders:
            if str(order.orderId) == str(orderId):
                announcement = f'Your order #{order.orderId} is sent to {order.location.city}. Total price: {order.price} UAH.'
                break
        if announcement:
            print(announcement)
        else:
            print(f'There is no order with #{orderId} number')