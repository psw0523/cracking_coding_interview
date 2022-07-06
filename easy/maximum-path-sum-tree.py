'''
Problem
Asked by Google

Given a binary tree of integers, find the maximum path sum between two nodes.
The path must go through at least one node, and does not need to go through the root
'''

'''
Solution

For example>
                          4
                      1       3
                   2    7   5   8
max sum is 11? (3+8)

Make tree as a array
Index  0   1    2    3    4    5   6   7
Value      4    1    3    2    7   5   8


left of n = 2n
right of n = 2n + 1
sum = 4+1 , 4+3, 1+2, 1+7, 3+5, 3+8
max = 3+8
'''

import math

def max_path_sum_on_tree(tree):
    length = len(tree)
    height = int(math.log2(len(tree) + 1))
    max_sum = 0 

    for i in range(1, height+1):
        my_idx = i
        left_idx = 2*i
        right_idx = 2*i + 1

        if left_idx >= length:
            return max_sum
        max_sum = max(max_sum, tree[my_idx] + tree[left_idx])

        if right_idx >= length:
            return max_sum
        max_sum = max(max_sum, tree[my_idx] + tree[right_idx])

    return max_sum


if __name__ == '__main__':
    print(max_path_sum_on_tree([None, 4, 1, 3, 2, 7, 5, 8]))
