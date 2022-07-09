def deletion(string):
    print(string[:string.index('h')] + string[string.rindex('h') + 1:])


deletion('Функція h отримує строку,h де літера')
