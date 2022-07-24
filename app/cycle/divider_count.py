def divider_counter(a):
    counter = 0
    for i in range(1, a + 1):
        if a % i == 0:
            counter = counter + 1
    return counter


