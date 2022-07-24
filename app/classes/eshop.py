class Item:
    def __init__(self, name: str, price: int, rate: int, quantity: int):
        self.name = name
        self.price = price
        self.rate = rate
        self.quantity = quantity


class Category:
    item = None

    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items

    def search(self, item):
        if item in self.items:
            return f'{item} is present'
        else:
            return f'There is no {item}'


class Basket:
    item = None

    def __init__(self, items: list):
        self.items = items

    def add(self, item):
        self.items.append(item)
        return f'{item} added to the basket'

    def delete(self, item):
        self.items.remove(item)
        return f'{item} removed from the basket'

    def checkout(self, item, user):
        if item.quantity == 0:
            return f'The last one {item.name} was bought'

        if item in self.items:
            if user.money >= item.price:
                item.quantity = item.quantity - 1
                user.money = user.money - item.price
                return f'You bought {item.name}'

            else:
                return "you don't have enough money"


class User:
    def __init__(self, login: str, pss: str, money: int, basket: Basket):
        self.login = login
        self.pss = pss
        self.money = money
        self.basket = basket


item_1 = Item('iphone', 999, 4, 45)
item_2 = Item('samsung', 980, 5, 87)
item_3 = Item('xiaomi', 500, 4, 120)
item_4 = Item('sony', 770, 3, 89)
item_5 = Item('oppo', 120, 3, 2)

item_list = [item_1, item_2, item_3, item_4, item_5]

user_1 = User('Peter', 'qwerty', 5, Basket(item_list))
user_2 = User('Lisa', '12345', 2000, Basket(item_list))
user_3 = User('Elizabeth', 'adfLJK&-3w', 1000, Basket(item_list))

user_list = [user_1, user_2, user_3]

user_2.basket.checkout(item_5, user_2)
user_2.basket.checkout(item_5, user_2)
user_2.basket.checkout(item_5, user_2)

item_5.quantity = 100
user_2.basket.checkout(item_5, user_2)


'''
['samsung', 980, 5, 87, 'Lisa', '12345', 2000, None, 'You bought oppo'],
['xiaomi', 500, 4, 120, 'Peter', 'qwerty', 5, None, 'The last one oppo was bought'],
['sony', 770, 3, 89, 'Lisa', '12345', 2000, None, 'You bought oppo'],
['oppo', 120, 3, 2, 'Peter', 'qwerty', 5, None, 'You bought oppo'],
'''