class User:
    login: str
    pss: str
    money: int

    def __init__(self, login: str, pss: str, money: int):

        self.login = login
        self.pss = pss
        self.money = money
