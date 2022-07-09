import pytest
from app.lists.even_indices import even_indices


@pytest.mark.parametrize(
    'a,  answer',
    [
        ((1, 2, 43, 2345, 1245, 32), [1, 43, 1245]),
    ]
)
def test_even_indices(a, answer):
    assert answer == even_indices(a)
