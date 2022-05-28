def is_permutation(str_a, str_b):
    # check size
    if len(str_a) == 0 or  len(str_b) == 0:
        return False

    a_map = dict()
    for a in str_a:
        if a not in a_map.keys():
            a_map[a] = 1
        else:
            val = a_map[a]
            val += 1
            a_map[a] = val

    a_keys = a_map.keys()
    for b in str_b:
        if b not in a_keys:
            return False
        else:
            val = a_map[b]
            val -= 1
            if val < 0:
                return False
            a_map[b] = val

    return True


if __name__ == '__main__':
    print(is_permutation("", "123"))
    print(is_permutation("321", "123"))
    print(is_permutation("54331", "1"))
    print(is_permutation("54331", "333"))
    print(is_permutation("54331", "3345"))
