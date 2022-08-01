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
    item = Item
    if __name__ == "__main__":
        from user_module import User
        user: User

    def __init__(self, items: list[Item]):
        self.items = items

    def set_user(self, usr):
        print(f'{usr} called')

    def add(self, item):
        self.items.append(item)
        print(f'{item} added to the basket')
        # return f'{item} added to the basket'

    def delete(self, item):
        self.items.remove(item)
        print(f'{item} removed from the basket')
        # return f'{item} removed from the basket'

    def checkout(self):
        if self.item == 0:
            print(f'The last one {self.item.name} was bought')
            # return f'The last one {item.name} was bought'

        if self.item in self.items:
            if user.money >= self.item.price:
                self.item.quantity = self.item.quantity - 1
                user.money = user.money - self.item.price
                print(f'You bought {self.item.name}')
                # return f'You bought {item.name}'

            else:
                print("you don't have enough money")
                # return "you don't have enough money"


if __name__ == "__main__":
    from user_module import User
    user: User

    item_1 = Item('iphone', 999, 4, 45)
    item_2 = Item('samsung', 980, 5, 87)
    item_3 = Item('xiaomi', 500, 4, 120)
    item_4 = Item('sony', 770, 3, 89)
    item_5 = Item('oppo', 120, 3, 2)

    item_list = [item_1, item_2, item_3, item_4, item_5]

    user_1 = User('Peter', 'qwerty', 5, Basket(item_list))
    user_2 = User('Lisa', '12345', 2000, Basket(item_list))
    user_3 = User('Elizabeth', 'adfLJK&-3w', 1000, Basket(item_list))

    basket = Basket(item_list)
    basket.set_user(user_1)

    basket.add(item_1)
    basket.checkout()


'''
user_list = [user_1, user_2, user_3]

user_2.basket.checkout(item_5, user_2)
user_2.basket.checkout(item_5, user_2)
user_2.basket.checkout(item_5, user_2)

item_5.quantity = 100
user_2.basket.checkout(item_5, user_2)


item_1 = Item('iphone', 999, 4, 45)
item_2 = Item('samsung', 980, 5, 87)
item_3 = Item('xiaomi', 500, 4, 120)
item_4 = Item('sony', 770, 3, 89)
item_5 = Item('oppo', 120, 3, 2)

item_list = [item_1, item_2, item_3, item_4, item_5]


item_1 = Item("name", 12, 12, 12)
items = [item_1]
basket = Basket(items)
basket.set_user("Petro")
'''