def leap_year(a: int) -> int:
    if not isinstance(a, int):
        raise TypeError(f'Argument "a" must be integer, not {type(a)}')

    if a % 4 == 0:
        return 'Yes'
    else:
        return 'No'


leap_year(2000)
