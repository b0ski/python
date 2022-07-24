import pytest
from app.classes.iphone import Iphone


@pytest.mark.parametrize(
    'model, weight, name, number, num_1, num_2, a1',
    [
        (6, 200, 'Boris', '555 - 777', '555 - 777', '555 - 888', '555 - 777'
         ),
    ]
)
def test_get_number(model: int, weight: int, name: str, number: str,
                    num_1: str, num_2: str, a1: str):
    iphone = Iphone(model, weight, name, number, num_1, num_2)
    assert iphone.getNumber() == a1


@pytest.mark.parametrize(
    'model, weight, name, number, num_1, num_2, a3',
    [
        (6, 200, 'Boris', '555 - 777', '555 - 777', '555 - 888', ('555 - 777', '555 - 888')
         ),
    ]
)
def test_send_message(model: int, weight: int, name: str, number: str, num_1: str, num_2: str, a3: str):
    iphone_1 = Iphone(model, weight, name, number, num_1, num_2)
    assert iphone_1.sendMessage(num_1, num_2) == a3


@pytest.mark.parametrize(
    'model, weight, name, number, num_1, num_2, a2',
    [
        (6, 200, 'Boris', '555 - 777', '555 - 777', '555 - 888', 'Boris is calling from 555 - 777 number',
         ),
    ]
)
def test_recieve_calls(model: int, weight: int, name: str, number: str, num_1: str, num_2: str, a2: str):
    iphone = Iphone(model, weight, name, number, num_1, num_2)
    assert iphone.recieveCall() == a2


