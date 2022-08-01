import pytest
from app.classes.eshop.operations_module import Item, Basket

if __name__ == "__main__":
    from app.classes.eshop.user_module import User
    user: User

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
