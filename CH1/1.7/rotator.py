from enum import Enum

class rotation_type(Enum):
    ROTATION_90 = 0
    ROTATION_180 = 1
    ROTATION_270 = 2
    ROTATION_FLIP = 3
    ROTATION_MAX = ROTATION_FLIP


class Rotator():
    def __init__(self, matrix, rot_type):
        if type(rot_type) is not rotation_type:
            raise ValueError('Invalid rotation type')

        if len(matrix) != len(matrix[0]):
            raise ValueError('matrix should be NxN')

        self.matrix = matrix
        self.rot_type = rot_type
        self.N = len(matrix)
        self.locations = set()
        for m in range(self.N):
            for n in range(self.N):
                self.locations.add((m,n))

    def get_target_location(self, l):
        column = l[0]
        row = l[1]

        if self.rot_type is rotation_type.ROTATION_90:
            target_column = self.N - 1 - row
            target_row = column
        elif self.rot_type is rotation_type.ROTATION_180:
            target_column = self.N - 1 - column
            target_row = self.N - 1 - row
        elif self.rot_type is rotation_type.ROTATION_270:
            target_column = row
            target_row = self.N - 1 - column
        elif self.rot_type is rotation_type.ROTATION_FLIP:
            target_column = self.N - 1 - column
            target_row = row

        return (target_column, target_row)

    def get_val(self, l):
        return self.matrix[l[0]][l[1]]

    def set_val(self, l, v):
        self.matrix[l[0]][l[1]] = v

    def already_moved(self, l):
        return not l in self.locations

    def next_source(self):
        return self.locations.pop()

    def rotate(self):
        steps = 0
        s = (0, 0)
        sval = self.get_val(s)
        while steps < self.N * self.N:
            if self.already_moved(s):
                s = self.next_source()
                sval = self.get_val(s)

            t = self.get_target_location(s)
            tval = self.get_val(t)
            self.set_val(t, sval)
            self.locations.discard(s)
            sval = tval
            s = t
            steps += 1

        return self.matrix


if __name__ == '__main__':
    rotator_90 = Rotator([[0,1,2],[3,4,5],[6,7,8]], rotation_type.ROTATION_90) 
    print(rotator_90.rotate())
    rotator_180 = Rotator([[0,1,2],[3,4,5],[6,7,8]], rotation_type.ROTATION_180) 
    print(rotator_180.rotate())
    rotator_270 = Rotator([[0,1,2],[3,4,5],[6,7,8]], rotation_type.ROTATION_270) 
    print(rotator_270.rotate())
    rotator_flip = Rotator([[0,1,2],[3,4,5],[6,7,8]], rotation_type.ROTATION_FLIP) 
    print(rotator_flip.rotate())

