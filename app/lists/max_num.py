def max_num(param):
    evens = []
    mx = []

    if len(param) == 1:
        return

    if len(param) % 2 != 0:
        param.append(0)

    for i in range(0, len(param)):
        if i % 2 == 0:
            evens.append(i)

    for x in evens:
        if param[x] < param[x + 1]:
            param[x], param[x + 1] = param[x + 1], param[x]
        mx.append(param[x])
    max_num(mx)
    return mx[0]


