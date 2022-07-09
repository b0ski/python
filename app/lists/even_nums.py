def even_nums(param):
    for instance in param:
        if instance % 2 == 0:
            print(instance)


even_nums((1, 2, 43, 2345, 1245, 32))
