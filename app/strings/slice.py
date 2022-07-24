def slice(a):
    print(a[2])
    print(a[len(a) - 2])
    print(a[:5])
    print(a[:-2])

    for char in a:
        if a.index(char) % 2 == 0:
            print(char)

    for char in a:
        if a.index(char) % 2 == 0:
            print(a[a.index(char) + 1])


slice('0123456789')
