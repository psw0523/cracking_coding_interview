'''
Problem
Asked by Google

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list.
You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1]
'''

'''
Solution

Remove the number over than k
and make Graph

12 1  5  9  2
1  5  9  2  12
5  9  2  12 1
9  2  12 1  5
2  12 1  5  9

DFS from 12
12 + 1 + 5 + 9 => Fail
12 + 1 + 5 + 2 + .. => Fail

How do traverse S?
12, 1, 5, 9, 2

12 -> 1 -> 5 -> 9 => Fail return 5
           5 -> 2 => Fail return 5, There is no other way from 5 return to 1, 5 is removed on S
        -> 9 -> 2 => if fail return 
...
'''

def do_sum(a, i, sub, sum, k):
    sum += a[i]
    sub.append(a[i])
    if sum == k:
        return True
    elif sum < k:
        i += 1
        if i == len(a):
            return False
        else:
            return sum(a, i, sub, sum, k)
