"""Location part of Logic System"""


class Location:
    """SImple class that create a place and post office for delivery"""
    def __init__(self, city, postoffice):
        self.city = city
        self.postoffice = postoffice

    def __repr__(self):
        return f'city: {self.city}, post office: {self.postoffice}'

    def __str__(self):
        return f'city: {self.city}, post office: {self.postoffice}'
