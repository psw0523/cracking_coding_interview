def compress_string(string):
    # order, count
    l = list()
    prev = 0
    num = 0
    for c in string:
        if c != prev:
            if prev != 0:
                append = prev + str(num)
                l.append(append)
            prev = c
            num = 1
        else:
            num += 1

    # for last repeat
    if num > 1:
        l.append(prev + str(num))

    compressed = ''.join(l)
    if len(compressed) >= len(string):
        return string
    return compressed


if __name__ == '__main__':
    print(compress_string("aaabb"))
    print(compress_string("abcd"))
    print(compress_string("aa"))
    print(compress_string("aaa"))
    print(compress_string("akdflldffffffcccccd"))
