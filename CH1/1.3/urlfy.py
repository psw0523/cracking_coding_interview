def urlfy(str_a, length):
    l = list()
    spaces = {' ', '\t', '\n'}

    for c in str_a:
        if c in spaces:
            l.append("%20")
        else:
            l.append(c)

    return ''.join(l)


if __name__ == '__main__':
    print(urlfy("Mr John Smith", 13))
    print(urlfy("Mr\tJohn\n\tSmith   \t Please stop", 13))
