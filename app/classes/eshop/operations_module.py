class User:
    login: str
    pss: str
    money: int

    def __init__(self, login: str, pss: str, money: int):
        self.login = login
        self.pss = pss
        self.money = money


class Item:
    name: str
    price: int
    rate: int
    quantity: int

    def __init__(self, name: str, price: int, rate: int, quantity: int):
        self.name = name
        self.price = price
        self.rate = rate
        self.quantity = quantity


class Category:
    name: str
    items: list = []
    item: Item = None

    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items

    def search(self, item):
        if item in self.items:
            return f'{item.name} is present'
        else:
            return f'There is no {item.name}'


class Basket:
    items: list[Item] = []
    user: User = None
    item: Item = None

    def __init__(self, items: list[Item]):
        self.items = items

    def set_user(self, login: str, pss: str, money: int):
        self.user = User(login, pss, money)
        return f'{self.user.login} is called'

    def add(self, item):
        self.items.append(item)
        self.item = item
        print(f'{item.name} added to the basket')
        return f'{item.name} added to the basket'

    def delete(self, item):
        self.items.remove(item)
        print(f'{item.name} removed from the basket')
        return f'{item.name} removed from the basket'

    def checkout(self):
        if self.item.quantity == 0:
            print(f'The last one {self.item.name} was bought')
            return f'The last one {self.item.name} was bought'
        
        if self.item in self.items:
            if self.user.money >= self.item.price:
                self.item.quantity = self.item.quantity - 1
                self.user.money = self.user.money - self.item.price
                print(f'You bought {self.item.name}')
                return f'You bought {self.item.name}'
        
            else:
                print("you don't have enough money")
                return "you don't have enough money"


item_1 = Item('iphone', 999, 4, 45)
item_2 = Item('samsung', 980, 5, 87)
item_3 = Item('xiaomi', 500, 4, 120)
item_4 = Item('sony', 770, 3, 89)
item_5 = Item('oppo', 120, 3, 2)

item_list = [item_1, item_2, item_3, item_4, item_5]

basket = Basket(item_list)
basket.set_user("Peter", "123", 1000)
basket.add(item_1)
basket.checkout()

