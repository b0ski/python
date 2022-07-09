def even_indices(param):
    for instance in param:
        if param.index(instance) % 2 == 0:
            print(instance)


even_indices((1, 2, 43, 2345, 1245, 32))
