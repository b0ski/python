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



