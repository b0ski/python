import pytest
from app.classes.eshop.operations_module import Item, Basket

item_1 = Item('iphone', 999, 4, 45)
item_2 = Item('samsung', 980, 5, 87)
item_3 = Item('xiaomi', 500, 4, 120)
item_4 = Item('sony', 770, 3, 89)
item_5 = Item('oppo', 120, 3, 2)

item_list = [item_1, item_2, item_3, item_4, item_5]


@pytest.fixture
def test_basket_add():
    basket = Basket(item_list)
    assert basket.add(item_1) == 'iphone added to the basket'
