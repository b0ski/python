from operations_module import Basket


class User:
    login: str
    pss: str
    money: int
    basket: Basket

    def __init__(self, login: str, pss: str, money: int, basket: Basket = None):

        self.login = login
        self.pss = pss
        self.money = money
        self.basket = basket

