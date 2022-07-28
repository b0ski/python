import user_module


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
    item = None

    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items

    def search(self, item):
        if item in self.items:
            print(f'{item} is present')
            # return f'{item} is present'
        else:
            print(f'There is no {item}')
            # return f'There is no {item}'


class Basket:
    items: list[Item] = []
    item = None
    user: user_module

    def __init__(self, items: list):
        self.items = items

    def add(self, item):
        self.items.append(item)
        print(f'{item} added to the basket')
        # return f'{item} added to the basket'

    def set_user(self, user):
        print(f'{user} called')

    def delete(self, item):
        self.items.remove(item)
        print(f'{item} removed from the basket')
        # return f'{item} removed from the basket'

    def checkout(self, item, user):
        if item.quantity == 0:
            print(f'The last one {item.name} was bought')
            # return f'The last one {item.name} was bought'

        if item in self.items:
            if user.money >= item.price:
                item.quantity = item.quantity - 1
                user.money = user.money - item.price
                print(f'You bought {item.name}')
                # return f'You bought {item.name}'

            else:
                print("you don't have enough money")
                # return "you don't have enough money"



  item_1 = Item(name, price, rate, quantity)


basket = Basket()
basket.set_user("Petro")