alphabetical = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
numerical = (1, 2, 3, 4, 5, 6, 7, 8)


def knight(k1, k2, t1, t2):
    coords = [[alphabetical.index(k1) + 2, numerical.index(k2) + 1],
              [alphabetical.index(k1) + 2, numerical.index(k2) - 1],
              [alphabetical.index(k1) + 1, numerical.index(k2) - 2],
              [alphabetical.index(k1) - 1, numerical.index(k2) - 2],
              [alphabetical.index(k1) - 2, numerical.index(k2) - 1],
              [alphabetical.index(k1) - 2, numerical.index(k2) + 1],
              [alphabetical.index(k1) - 1, numerical.index(k2) + 2],
              [alphabetical.index(k1) + 1, numerical.index(k2) + 2]]

    for pair in coords:

        if alphabetical[pair[0]] == t1 and numerical[pair[1]] == t2:
            return "Yes"

        else:
            return 'No'

