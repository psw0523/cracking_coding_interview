def check_permu_of_palrin(string):
    # Parlindrome: same even characters and only one odd character
    # ex> aabbbaa -> ababbaa, aaaabbb
    # ex> aabbbcccbbbaa ->
    if len(string) <= 1:
        return False

    m = dict()
    for c in string:
        if c not in m.keys():
            m[c] = 1
        else:
            val = m[c]
            val += 1
            m[c] = val

    odd_num = 0
    for k,v in m.items():
        if v % 2 == 1:
            odd_num += 1
            if odd_num > 1:
                return False

    return True


if __name__ == '__main__':
    print(check_permu_of_palrin(""))
    print(check_permu_of_palrin("abba"))
    print(check_permu_of_palrin("aabba"))
    print(check_permu_of_palrin("aabbbaa"))
    print(check_permu_of_palrin("aabbbcccaa"))
    print(check_permu_of_palrin("aabbbcccbbbaa"))
