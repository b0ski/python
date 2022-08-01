import pytest
from app.classes.eshop.eshop import Item, Basket, User


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


