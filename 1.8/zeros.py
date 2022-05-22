def make_zeros(matrix):
    zero_columns = set()
    zero_rows = set()

    m = 0
    #  n = 0
    while m < len(matrix):
        for n in range(len(matrix[0])):
            if matrix[m][n] == 0:
                zero_columns.add(m)
                zero_rows.add(n)
                break
        m += 1

    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            if m in zero_columns or n in zero_rows:
                matrix[m][n] = 0

    return matrix


if __name__ == '__main__':
    print(make_zeros([[1,2,3],[4,5,6],[0,8,9]]))
