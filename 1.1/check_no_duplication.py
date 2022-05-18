def check_no_duplication(string):
    s = set()
    for c in string:
        if c not in s:
            s.add(c)
        else:
            return False
    return True


def check_no_duplication_without_dsa(string):
    # Only alphabet can be the character in string?
    # Will use the bitmap for alphabet
    bitmap = 0
    for c in string:
        intval = 1 << ord(c)
        if bitmap & intval:
            return False
        else:
            bitmap |= intval
    return True


if __name__ == "__main__":
    #  print(check_no_duplication("12345"))  # should display True
    #  print(check_no_duplication("11345"))  # should display False
    #  print(check_no_duplication(""))  # should display True
    #  print(check_no_duplication("1"))  # should display True
    #  print(check_no_duplication("aA"))  # should display True
    print(check_no_duplication_without_dsa("12345"))  # should display True
    print(check_no_duplication_without_dsa("11345"))  # should display False
    print(check_no_duplication_without_dsa(""))  # should display True
    print(check_no_duplication_without_dsa("1"))  # should display True
    print(check_no_duplication_without_dsa("aA"))  # should display True
