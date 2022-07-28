import eshop


class User:
    login: str
    pss: str
    money: int
    basket: eshop.Basket

    def __init__(self, login: str, pss: str, money: int):
        """'
        self.login = login
         self.pss = pss
         self.money = money
         self.basket = basket
        '"""
