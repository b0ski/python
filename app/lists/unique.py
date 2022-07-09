def unique(param):
    for instance in param:
        if param.count(instance) == 1:
            print(instance)


unique([1, 22, 22, 11, 11, 11, 22, 333])
