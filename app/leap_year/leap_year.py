def greater(a: int) -> int:
    if not isinstance(a, int):
        raise TypeError(f'Argument "a" must be integer, not {type(a)}')


    if a%4 == 0:
        print (“Yes”)
    else:
        print (“Yes”)

