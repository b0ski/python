def even_numbers(a, b):
    arr = []
    for i in range(a, b):
        if i % 2 == 0:
            arr.append(i)
    return arr


