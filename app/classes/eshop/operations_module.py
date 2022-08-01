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
        return f'{item} added to the basket'

    def delete(self, item):
        self.items.remove(item)
        print(f'{item} removed from the basket')
        # return f'{item} removed from the basket'

    def checkout(self):
        if self.item == 0:
            return f'The last one {self.item.name} was bought'

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


@pytest.mark.parametrize(
    'name, price, rate, quantity, login, pss, money, basket, ans',
    [
        ('iphone', 999, 4, 45, 'Peter', 'qwerty', 5, None, 'you don\'t have enough money'),
        ('samsung', 980, 5, 87, 'Lisa', '12345', 2000, None, 'You bought samsung'),

    ]
)
def test_checkout(name: str, price: int, rate: int, quantity: int, login: str, pss: str, money: int, basket: Basket, ans):
    item_1 = Item(name, price, rate, quantity)
    item_list = [item_1]
    user_1 = User(login, pss, money, Basket(item_list))
    user_1.basket.checkout(item_1, user_1)
    assert user_1.basket.checkout(item_1, user_1) == ans


@pytest.mark.parametrize(
    'name_1, price_1, rate_1, quantity_1, login_1, pss_1, money_1, basket_1,'
    'name_2, price_2, rate_2, quantity_2, login_2, pss_2, money_2, basket_2, ans',
    [
        ('iphone', 999, 4, 1, 'Peter', 'qwerty', 1000, None,
         'samsung', 980, 5, 87, 'Lisa', '12345', 2000, None, 'The last one iphone was bought'),
    ]
)
def test_last_phone(name_1: str, price_1: int, rate_1: int, quantity_1: int, login_1: str, pss_1: str, money_1: int, basket_1: Basket,
                    name_2: str, price_2: int, rate_2: int, quantity_2: int, login_2: str, pss_2: str, money_2: int, basket_2: Basket,
                    ans):
    item_1 = Item(name_1, price_1, rate_1, quantity_1)
    item_list = [item_1]

    user_1 = User(login_1, pss_1, money_1, Basket(item_list))
    user_2 = User(login_2, pss_2, money_2, Basket(item_list))

    user_1.basket.checkout(item_1, user_1)
    user_2.basket.checkout(item_1, user_2)
    assert user_1.basket.checkout(item_1, user_1) == ans





@pytest.fixture
def user_1() -> User:
    user_1 = User('Peter', 'qwerty', 5, Basket(item_list))
    return user_1


@pytest.fixture
def item_1() -> Item:
    item_1 = Item('iphone', 999, 4, 45)
    return item_1


@pytest.fixture
def item_2() -> Item:
    item_2 = Item('samsung', 980, 5, 87)
    return item_2


@pytest.fixture
def item_3() -> Item:
    item_3 = Item('xiaomi', 500, 4, 120)
    return item_3


item_list = [item_1(), item_2(), item_3()]


@pytest.fixture
def basket(item_1) -> Basket:
    basket = Basket(item_list)
    return basket


def test_basket_add(basket, item_1):
    assert basket.checkout(item_1) == 'iphone added to the basket'








@pytest.fixture
def user_1() -> User:
    user_1 = User('Peter', 'qwerty', 5, Basket(item_list))
    return user_1


'''