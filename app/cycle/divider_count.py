def divider_counter(a):
    counter = 0
    for i in range(1, a):
        if a % i == 0:
            counter = counter + 1
    print(counter)


divider_counter(12)
