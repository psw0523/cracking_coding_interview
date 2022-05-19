def can_make_same_string_by_just_one_operation(a_string, b_string):
    # check the length: the size difference should not bigger than 1
    len_diff = len(a_string) - len(b_string)
    if abs(len_diff) > 1:
        return False

    length_of_loop = len(b_string) if len(a_string) >= len(b_string) else len(a_string)

    diff_num = 0
    if len_diff != 0:
        diff_num += 1

    for i in range(length_of_loop):
        if a_string[i] != b_string[i]:
            diff_num += 1
            if diff_num > 1:
                return False

    return True


if __name__ == '__main__':
    print(can_make_same_string_by_just_one_operation("mike", "Mike"))
    print(can_make_same_string_by_just_one_operation("mike", "Make"))
    print(can_make_same_string_by_just_one_operation("mike", "make"))
    print(can_make_same_string_by_just_one_operation("m", "M"))
    print(can_make_same_string_by_just_one_operation("", "M"))
    print(can_make_same_string_by_just_one_operation("aka", "aKaa"))
