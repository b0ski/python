class Iphone:
    def __init__(self, model, weight, name, number='Unknown number'):
        self.number = number
        self.model = model
        self.weight = weight
        self.name = name

    def __str__(self):
        return self.number, self.model, self.weight

    def recieveCall(self):
        print(f'{self.name} is calling from {self.number} number')

    def getNumber(self):
        print(self.number)

    def sendMessage(self, *args):
        print(*args)


phone_1 = Iphone('555 - 777', 6, 200, 'Boris')
phone_2 = Iphone('555 - 777', 7, 100, 'Petro')
phone_3 = Iphone('555 - 888', 8, 160, 'Stepan')

print(phone_1.__str__())

phone_1.recieveCall()
phone_1.getNumber()
phone_2.getNumber()
phone_3.getNumber()

phone_3.sendMessage('555 - 777', '555 - 888')
