class Item:
    def __init__(self, name: str, price: int, rate: int, quantity: int):
        self.name = name
        self.price = price
        self.rate = rate
        self.quantity = quantity


class Category:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items


class Basket:
    def __init__(self, items: list):
        self.items = items

    def add(self):
        print('added')

    def delete(self):
        print('deleted')


class User:
    def __init__(self, login: str, pss: str, basket: Basket):
        self.login = login
        self.pss = pss
        self.basket = basket

