import pytest
from app.classes.cars import Driver, Engine, Car, Lorry, SportCar


@pytest.mark.parametrize(
    'firstName, lastName, power, manufacturer, exp, model, clss, weight, driver, engine, ans',
    [
        ('Petro', 'Petrenko',
         60, 'fiat',
         2000, 'Orneo', 's', 1000, None, None, 'Поїхали'
         ),
    ]
)
def test_start(firstName: str, lastName: str,
               power: int, manufacturer: str,
               exp: int, model: str, clss: str, weight: int, driver: Driver, engine: Engine, ans):
    driver = Driver(firstName, lastName, exp)
    engine = Engine(power, manufacturer)
    car = Car(model, clss, weight, driver, engine)
    assert car.start() == ans


@pytest.mark.parametrize(
    'firstName, lastName, power, manufacturer, exp, model, clss, weight, driver, engine, ans',
    [
        ('Petro', 'Petrenko',
         60, 'fiat',
         2000, 'Orneo', 's', 1000, None, None, 'Зупиняємось'
         ),
    ]
)
def test_stop(firstName: str, lastName: str,
              power: int, manufacturer: str,
              exp: int, model: str, clss: str, weight: int, driver: Driver, engine: Engine, ans):
    driver = Driver(firstName, lastName, exp)
    engine = Engine(power, manufacturer)
    car = Car(model, clss, weight, driver, engine)
    assert car.stop() == ans


@pytest.mark.parametrize(
    'firstName, lastName, power, manufacturer, exp, model, clss, weight, driver, engine, ans',
    [
        ('Petro', 'Petrenko',
         60, 'fiat',
         2000, 'Orneo', 's', 1000, None, None, 'Поворот праворуч'
         ),
    ]
)
def test_turnRight(firstName: str, lastName: str,
                   power: int, manufacturer: str,
                   exp: int, model: str, clss: str, weight: int, driver: Driver, engine: Engine, ans):
    driver = Driver(firstName, lastName, exp)
    engine = Engine(power, manufacturer)
    car = Car(model, clss, weight, driver, engine)
    assert car.turnRight() == ans


@pytest.mark.parametrize(
    'firstName, lastName, power, manufacturer, exp, model, clss, weight, driver, engine, ans',
    [
        ('Petro', 'Petrenko',
         60, 'fiat',
         2000, 'Orneo', 's', 1000, None, None, 'Поворот ліворуч'
         ),
    ]
)
def test_turnLeft(firstName: str, lastName: str,
                  power: int, manufacturer: str,
                  exp: int, model: str, clss: str, weight: int, driver: Driver, engine: Engine, ans):
    driver = Driver(firstName, lastName, exp)
    engine = Engine(power, manufacturer)
    car = Car(model, clss, weight, driver, engine)
    assert car.turnLeft() == ans
