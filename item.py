"""Part of Logic System"""


class Item:
    """The specific description of product that you need"""
    def __init__(self, name: str, price: str):
        self.name = name
        self.price = price

    def __str__(self):
        return f'name: {self.name}\nprice: {self.price} UAH'

    def __repr__(self):
        return f'name: {self.name}\nprice: {self.price} UAH'
