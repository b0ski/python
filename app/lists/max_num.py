def max_num(param):
    evens = []
    max = []

    if len(param) == 1:
        print(param)
        return param

    if len(param) % 2 != 0:
        param.append(0)

    for i in range(0, len(param)):
        if i % 2 == 0:
            evens.append(i)

    for x in evens:
        if param[x] < param[x + 1]:
            param[x], param[x + 1] = param[x + 1], param[x]
        max.append(param[x])
    max_num(max)


max_num([1, 2, 3])

