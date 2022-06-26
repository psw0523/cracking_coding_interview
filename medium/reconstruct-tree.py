"""
Asked by Google

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:
[a, b, d, e, c, f, g]
And the following in order traversal:
[d, b, e, a, f, c, g]
You should return the following tree:
     a
    / \
   b   c
  / \ / \
 d  e f  g
"""

"""
Solution

1, 2, 3, 4, 5, 6, 7

Firstly make the binary tree

         4
      2     6
    1  3   5  7

We can express tree as array starting index 1
left child : parent index * 2
right child : parent index * 2 + 1
index 0  1  2  3  4  5  6  7
value    4  2  6  1  3  5  7

We can run preorder this tree

index 0  1  2  3  4  5  6
value 4  2  1  3  6  5  7

From this, we can make the map the preorder position -> tree position

0 -> 1
1 -> 2
2 -> 4
3 -> 5
4 -> 3
5 -> 6
6 -> 7

    0  1  2  3  4  5  6  
So [a, b, d, e, c, f, g]
Tree
Index   0  1  2  3  4  5  6  7
value      a  b  c  d  e  f  g

We can also run inorder this tree

index 0  1  2  3  4  5  6
value 1  2  3  4  5  6  7

    3  -> 1
    3  -> 5

index 0  1  2  3  4  5  6  7
value    1  2  3  4  5  6  7

This is easy
Inorder traversal ouput is the ordered array.

[d, b, e, a, f, c, g]

Write function make_binary_tree_from_ordered_array(array, tree)

make_tree(array, n, tree, i):
    if i > len(array):
       return
    tree[i] = array[n]
    make_tree(array, n / 2, tree, i * 2)
    make_tree(array, n + n / 2, tree, i * 2 + 1)

  tree[1] = array[n/2]
  tree[2] = left of root
   tree.append(array[n/2])
   root = array[n/2]
   root.left = 

Question: preorder, inorder traversal all given? Or only one is given?

                           8
                4                       11
        2           6            9             13
    1      3     5     7      8   10        12    14
"""

def make_tree(array, l, r, tree, i, d = None):
    #  print(l, r, i)
    if i > len(array) or l == r or r > len(array):
        return
    c = (l + r) >> 1
    #  print(l, r, c, i)
    tree[i] = array[c]
    if d is not None:
        d[array[c]] = i
    #  print(tree)
    make_tree(array, l, c, tree, i * 2, d)
    make_tree(array, c, r + 1 if (c + r) % 2 else r, tree, i * 2 + 1, d)


def preorder(t, n, r):
    if (n >= len(t)):
        return
    r.append(t[n])
    preorder(t, n * 2, r)
    preorder(t, n * 2 + 1, r)


#[a, b, d, e, c, f, g]
class TreeFromPreorder():
    def __init__(self, length):
        # make tree
        a = [i for i in range(1, length + 1)]
        t = [0] * (length + 1)
        self.d = dict()
        make_tree(a, 0, length - 1, t, 1, self.d)
        print("d -> ", self.d)
        self.m = dict()
        preordered = list()
        preorder(t, 1, preordered)
        print("preordered => ", preordered)
        for i in range(len(preordered)):
            self.m[i] = self.d[preordered[i]]
        print(self.m)

    def get_tree(self, preordered):
        r = [0 for i in range(len(preordered) + 1)]
        for i in range(len(preordered)):
            r[self.m[i]] = preordered[i]
        return r


if __name__ == '__main__':
    problem = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
    engine = TreeFromPreorder(len(problem))
    print(engine.get_tree(problem))

    #  array = [1, 2, 3, 4, 5, 6, 7]
    #  print(array)
    #  tree = [0] * (len(array) + 1)
    #  make_tree(array, 0, len(array) - 1, tree, 1)
    #  print(tree)
#
    #  array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    #  print(array)
    #  tree = [0] * (len(array) + 1)
    #  make_tree(array, 0, len(array) - 1, tree, 1)
    #  print(tree)
#
    #  array = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
    #  print(array)
    #  tree = [0] * (len(array) + 1)
    #  make_tree(array, 0, len(array) - 1, tree, 1)
    #  print(tree)
#
    #  preordered = list()
    #  preorder(tree, 1, preordered)
    #  print(preordered)
