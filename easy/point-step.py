'''
Problem
Asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:

    (x,y) to
      (x+1, y)
      (x-1, y)
      (x, y+1)
      (x, y-1)
      (x-1,y-1)
      (x+1,y+1)
      (x-1,y+1)
      (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it.
You start from the first point.

Example:
    Input: [(0,0), (1,1), (1,2)]
    Output: 2
'''

'''
Solution

첫번째 포인트에서부터 다음과 같이 한다.
(x1, y1) -> (x2, y2)

- 방향 결정: x direction, y direction
x2 - x1 >= 0 => +
x2 - x1 <  0 => -
- 한번에 움직일 수 있는 크기 결정: x size, y size
abs(x2 - x1) >= MAX => MAX => 1 
abs(y2 - y1) >= MAX => MAX => 1 

- 구조
  cur = input[0]
  steps = 0
  for i in range(1, len(input)):
    next = input[i]
    steps += move_to(cur, next)
    cur = next

  return steps

  move_to(cur, next):
    steps = 0
    while cur.x != next.x or cur.y != next.y:
        x_diff = next.x - cur.x
        y_diff = next.y - cur.y
        x_direction = -1 if x_diff < 0 else 1
        y_direction = -1 if y_diff < 0 else 1
        x_size = 1 if abs(x_diff) > 1 else abs(x_diff)
        y_size = 1 if abs(y_diff) > 1 else abs(y_diff)
        move(cur, x_direction, x_size, y_direction, y_size)
        step += 1

  move(cur, x_direction, x_size, y_direction, y_size):
    cur.x += x_direction * x_size
    cur.y += y_direction * y_size
'''

def move(cur, x_direction, x_size, y_direction, y_size):
    return (cur[0] + x_direction * x_size, cur[1] + y_direction * y_size)

# cur, next: (x, y) tuple
def move_to(cur, next):
    steps = 0
    while cur[0] != next[0] or cur[1] != next[1]:
        x_diff = next[0] - cur[0]
        y_diff = next[1] - cur[1]
        x_direction = -1 if x_diff < 0 else 1
        y_direction = -1 if y_diff < 0 else 1
        x_size = 1 if abs(x_diff) > 1 else abs(x_diff)
        y_size = 1 if abs(y_diff) > 1 else abs(y_diff)
        cur = move(cur, x_direction, x_size, y_direction, y_size)
        steps += 1
    return steps

# points : list of (x,y) tuple
# return steps to cover all points
def cover(points):
    cur = points[0]
    steps = 0
    for i in range(1, len(points)):
        next = points[i]
        steps += move_to(cur, next)
        cur = next
    return steps


if __name__ == '__main__':
    print(cover([(0,0), (1,1), (1,2)]))
    print(cover([(0,0), (-2,1), (1,2)]))
