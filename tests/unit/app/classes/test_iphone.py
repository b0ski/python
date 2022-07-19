import pytest
from app.classes.iphone import Iphone


@pytest.mark.parametrize(

    'model, weight, name, number, num_1, num_2,'
    # answers
    'a1,'
    'a2,'
    'a3',

    [
        (6, 200, 'Boris', '555 - 777', '555 - 777', '555 - 888',
         # answers
         '555 - 777',
         'Boris is calling from 555 - 777 number',
         ('555 - 777', '555 - 888')

         ),
    ]
)
def test_operations(model: int, weight: int, name: str, number: str,
                    num_1: str, num_2: str, a1: str, a2: str, a3: str):
    iphone = Iphone(model, weight, name, number, num_1, num_2)
    assert iphone.getNumber() == a1
    assert iphone.recieveCall() == a2
    assert iphone.sendMessage(num_1, num_2) == a3


