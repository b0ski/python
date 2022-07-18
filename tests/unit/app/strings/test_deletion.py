import pytest
from app.strings.deletion import deletion


@pytest.mark.parametrize(
    'a,  answer',
    [
        ('Функція h отримує строку,h де літера', 'Функція  де літера'),
        ('hhohoho', 'o'),
        ('aaaaaaaa', 'There is no \'h\' in the string'),
    ]
)
def test_deletion(a, answer):
    assert answer == deletion(a)
