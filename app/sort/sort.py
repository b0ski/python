def max_in_pairs(param):
    evens = []
    min = []

    if len(param) == 1:
        return

    if len(param) % 2 != 0:
        param.append(0)

    for i in range(0, len(param)):
        if i % 2 == 0:
            evens.append(i)

    for x in evens:
        if param[x] > param[x + 1]:
            param[x], param[x + 1] = param[x + 1], param[x]
        min.append(param[x])
        print(min)

    max_in_pairs(min)


max_in_pairs([110, 2, 45, 132, 82, 9, 22, 3])










