'''
Problem
Asked by Google.

You are given a list of rectangles representing by min and max x- and y- coordinates.
Compute whether or not a pair of rectangles overlap each other.
If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:
    start x-y   width-height
    (1,4)        (3,3)
    (-1,3)       (2,1)
    (0,5)        (4,3)

return true as the first and third rectangle overlap each other.
'''

'''
Solution

A (1,4) (3,3) => 

(1,7) -- (4,7)
  |        |
(1,4) -- (4,4)

compare each two rectangles 

inputs = list of (x,y,w,h)

for i in range(len(inputs)):
    a = inputs[i]
    j = i + 1
    while j < len(inputs):
      b = inputs[j]
      if is_overlapping(a, b):
         return True

return False

is_overlapping(a, b):
    # check a.x 
    if overlap(a.x, a.x+a.w, b.x, b.x + b.w) and (a.y, a.y + a.h, b.y, b.y + b.h):
       return True

overlap(s1, e1, s2, e2):
    if s1 > s2 and s1 < e2:
       return True
    if s2 > s1 and s2 < e1:
       return True
    return False
'''

# Brute force implementation
def overlap(s1, e1, s2, e2):
    if s1 > s2 and s1 < e2:
        return True
    if s2 > s1 and s2 < e1:
        return True
    return False


def is_overlapping(a, b):
    if overlap(a[0], a[0]+a[2], b[0], b[0]+b[2]) and overlap(a[1], a[1]+a[3], b[1], b[1]+b[3]):
        return True
    return False


def check_overlapping(inputs):
    for i in range(len(inputs)):
        a = inputs[i]
        j = i + 1
        while j < len(inputs):
            b = inputs[j]
            if is_overlapping(a, b):
                return True
            j += 1
    return False


if __name__ == '__main__':
    inputs = [(1,4,3,3), (-1,3,2,1),(0,5,4,3)]
    print(check_overlapping(inputs))

    inputs = [(1,4,3,3), (-1,3,2,1),(0,5,1,3)]
    print(check_overlapping(inputs))
