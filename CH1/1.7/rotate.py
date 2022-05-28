def rotate(pixels):
    if len(pixels) != len(pixels[0]):
        raise ValueError('pixel array list should be NxN')

    N = len(pixels)
    target = list()
    for i in range(N):
        target.append([0]*N)

    # left 90 degree
    for m in range(N):
        for n in range(N):
            target[N - 1 - n][m] = pixels[m][n]

    return target


def get_target_location(num_of_column, source_location):
    ''' input
        num: number of column
        source_location: tuple (column, row) -> ex> (0, 0)
        return target (column, row) '''
    source_column = source_location[0]
    source_row = source_location[1]
    target_column = num_of_column - 1 - source_row
    target_row = source_column
    return (target_column, target_row)


def set_val(matrix, location, val):
    matrix[location[0]][location[1]] = val


def get_val(matrix, location):
    return matrix[location[0]][location[1]]


def already_handled(location, sets):
    return not location in sets


def rotate2(pixels):
    ''' Do not use an additional matrix
    '''
    if len(pixels) != len(pixels[0]):
        raise ValueError('pixel array list should be NxN')

    N = len(pixels)

    locations = set()
    for m in range(N):
        for n in range(N):
            locations.add((m,n))
    
    s = (0, 0) # source location
    sval = get_val(pixels, s)
    steps = 0
    while steps < N * N:
        if already_handled(s, locations):
            s = locations.pop() # get next source location
            sval = get_val(pixels, s)

        t = get_target_location(N, s) # t is target location
        tval = get_val(pixels, t)
        set_val(pixels, t, sval)
        locations.discard(s)
        sval = tval 
        s = t
        steps += 1

    return pixels


if __name__ == '__main__':
    #  print(rotate([[0,1,2],[3,4,5],[6,7,8]]))
    #  print(rotate([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]))
    #  print(rotate([[0,1,2],[3,4,5]]))

    print(rotate2([[0,1,2],[3,4,5],[6,7,8]]))
    print(rotate2([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]))
