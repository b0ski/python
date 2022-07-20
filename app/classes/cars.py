class Driver:
    def __init__(self, firstName: str, lastName: str, exp: int):
        self.firstName = firstName
        self.lastName = lastName
        self.exp = exp


class Engine:
    def __init__(self, power: int, manufacturer: str):
        self.power = power
        self.manufacturer = manufacturer


class Car:
    def __init__(self, model: str, clss: str, weight: int, driver: Driver, engine: Engine):
        self.model = model
        self.clss = clss
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def __str__(self):
        return self.model, self.clss, self.weight, self.driver, self.engine

    def start(self):
        print("Поїхали")

    def stop(self):
        print("Зупиняємось")

    def turnRight(self):
        print("Поворот праворуч")

    def turnLeft(self):
        print("Поворот ліаворуч")


class Lorry(Car):
    def __init__(self, carrying_capacity: int, model: str, clss: str, weight: int, driver: Driver, engine: Engine):
        super().__init__(model, clss, weight, driver, engine)
        self.carrying_capacity = carrying_capacity


class SportCar(Car):
    def __init__(self, speed: int, model: str, clss: str, weight: int, driver: Driver, engine: Engine):
        super().__init__(model, clss, weight, driver, engine)
        self.speed = speed
