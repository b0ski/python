class Iphone:
    def __init__(self, model: int, weight: int, name: str,
                 number: str = 'Unknown number', *args):
        self.number = number
        self.model = model
        self.weight = weight
        self.name = name
        self.args = args

    def __str__(self):
        return self.number, self.model, self.weight

    def recieveCall(self):
        return f'{self.name} is calling from {self.number} number'

    def getNumber(self):
        return self.number

    def sendMessage(self, *args: str):
        return args


phone_1 = Iphone(6, 200, 'Boris', '555 - 777')


'''

phone_2 = Iphone('555 - 777', 7, 100, 'Petro')
phone_3 = Iphone('555 - 888', 8, 160, 'Stepan')

print(phone_1.__str__())


phone_1.getNumber()
phone_2.getNumber()
phone_3.getNumber()

'''

phone_1.sendMessage('555 - 777', '555 - 888')


