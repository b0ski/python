import pytest
from app.classes.iphone import Iphone


@pytest.mark.parametrize(
    'model, weight, name, number, answer',
    [
        (6, 200, 'Boris', '555 - 777', '555 - 777'),
    ]
)
def test_operations(model, weight, name, number, answer):
    iphone = Iphone(model, weight, name, number)
    assert iphone.getNumber() == answer






#Boris is calling from 555 - 777 number