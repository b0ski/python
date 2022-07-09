def even_indices(param):
    arr = []
    for instance in param:
        if param.index(instance) % 2 == 0:
            arr.append(instance)
    return arr



