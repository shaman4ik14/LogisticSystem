"""Vehicle part of Logic System"""

last_id = 0
station = []

class Vehicle:
    """Show the transport that will deliver your order.
    Also account that this transport can be busy"""
    def __init__(self, vehicleNo: str, isAvailable=True):
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable
        global last_id
        last_id += 1
        self.number = last_id
        global station
        station.append(self)

    def __repr__(self):
        condition = self.isAvailable
        if self.isAvailable == True:
            condition = 'free'
        return f'name: {self.vehicleNo}, condition: {condition}'

    def __str__(self):
        condition = self.isAvailable
        if self.isAvailable == True:
            condition = 'free'
        return f'name: {self.vehicleNo}, condition: {condition}'
