def even_indices(param):
    for char in param:
        if param.index(char) % 2 == 0:
            print(char)


even_indices((1, 2, 43, 2345, 1245, 32))
