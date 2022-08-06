def unique(param):
    arr = []
    for instance in param:
        if param.count(instance) == 1:
            arr.append(instance)
    return arr



