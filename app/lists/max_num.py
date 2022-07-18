def max_num(param):
    evens = []
    max = []
    result = 0

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
        max.append(param[x])
    print(max)

    max_num(max)
  #  return max


max_num([1100, 2, 45, 132, 82, 9, 22, 3])

