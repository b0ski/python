import pytest
from app.classes.eshop.operations_module import Item, Basket


@pytest.fixture
def item_1() -> Item:
    item_1 = Item('iphone', 999, 4, 45)
    return item_1


def item_2() -> Item:
    item_2 = Item('samsung', 980, 5, 87)
    return item_2


def item_3() -> Item:
    item_3 = Item('xiaomi', 500, 4, 120)
    return item_3


def item_4() -> Item:
    item_4 = Item('sony', 770, 3, 89)
    return item_4


def item_5() -> Item:
    item_5 = Item('oppo', 120, 3, 2)
    return item_5


@pytest.fixture
def item_list() -> list:
    item_list = [item_1, item_2, item_3, item_4, item_5]
    return item_list


@pytest.fixture
def basket(item_list) -> Basket:
    basket = Basket(item_list)
    return basket


def test_basket_add(basket, item_1):
    b_add = basket.add(item_1)
    assert b_add == 'iphone added to the basket'


def test_user(basket):
    set_user = basket.set_user("Peter", "123", 100)
    assert set_user == 'Peter is called'


def test_check(basket):
    check = basket.checkout()
    assert check == 'You bought iphone'






