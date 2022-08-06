def divider(a):
    arr = []
    for i in range(1, a):
        if a % i == 0:
            arr.append(i)
    return arr
