'''
Problem
Given a number in the form of a list of digits, return all possible permutations.
For example, given [1,2,3], return
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

'''
Solution
                               [1,2,3]
   1, [2, 3]            2,[1,3]               3,[1,2]
1,2,[3]   1,3,[2]   2,1,[3]  2,3,[1]      3,1,[2]   3,2,[1]
1,2,3     1,3,2     2,1,3    2,3,1        3,1,2     3,2,1

function permutate(a, l, r)
for i in range(len(a)):
   c = a[i]
   a.remove(c)
   l.append(a)
        permutate(a, l, r)
   a.append(c)

a = 1,2,3
l = []

step 1:
a = 2,3
l = 1

step 2 - 1:
a = 3
l = 1,2

step 2 - 2:


'''

def permutate(a, l, r):
    if len(a) == 0:
        r.append(l)
        return

    lists = [list(l) for i in range(len(a))]
    print(lists)

    for i in range(len(a)):
        c = a[0]
        a.remove(c)
        print(c)
        l = lists[i]
        l.append(c)
        permutate(a, l, r)
        a.append(c)



if __name__ == '__main__':
    a = [1,2,3]
    r = list()
    permutate(a, list(), r)
    print(r)
