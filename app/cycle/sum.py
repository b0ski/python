def sum(*args):
    counter = 0
    for number in args:
        counter = counter + number
        print(counter)


sum(1, 1, 1)
