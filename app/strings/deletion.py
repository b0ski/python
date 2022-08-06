def deletion(string):
    if string.count('h') == 0:
        return 'There is no \'h\' in the string'

    return string[:string.index('h')] + string[string.rindex('h') + 1:]




