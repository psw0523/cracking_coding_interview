def is_rotated(s1, s2):
    ''' check whether s1 is rotated string of s2
    '''
    # length should be same
    if len(s1) != len(s2):
        raise ValueError('Length of two strings should be same')

    # question: character can be shown more than once?
    
    chars = set()
    for c in s1:
        chars.add(c)

    for c in s2:
        if c not in chars:
            return False
        chars.remove(c)

    if len(chars) > 0:
        return False

    return True


if __name__ == '__main__':
    print(is_rotated('abcde', 'ecbad'))
    print(is_rotated('abcde', 'acbad'))
