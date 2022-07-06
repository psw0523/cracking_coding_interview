'''
Problem
Asked by Google.

A girl is walking along an apple orchard with a bag in each hand.
She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.
'''

'''
Solution

for each input, add type to set, but preserve the latest added type.
If the length of set is over 2, remove the type that is not latest,
preserve the subarray.

function add_type(type, set, latest, sub, max_sub)
  if len(set) == 2 and type not in set
     remove type that is not latest on set
     if len(sub) > max_sub
       max_sub = sub
     sub.clear()
     sub.append(latest)

  set.add(type)
  sub.append(type)
  return type


main
   inputs = [2, 1, 2, 3, 3, 1, 3, 5]
   max_sub = []
   sub = []
   latest = None
   s = set()
   for type in inputs
     latest = add_type(type, s, latest)
'''

'''
TODO implement as class
'''

def add_type(a, s, left, right, cur, max_sub):
    # return max_sub
    print(left, right, cur)
    if len(s) == 2 and a[cur] not in s:
        print(left, right, cur)
        if (right - left + 1) > len(max_sub):
            max_sub = a[left:right+1]
            print("max_sub", max_sub)
        right_value = a[right]
        idx = right
        while idx >= left and a[idx] == right_value:
            idx -= 1
        left = idx + 1
        s.remove(a[left-1])

    s.add(a[cur])
    right = cur

    return left, right, max_sub


if __name__ == '__main__':
    input_array = [2, 1, 2, 3, 3, 1, 3, 5]
    s = set()
    max_sub = []
    left = 0
    right = 0
    for i in range(len(input_array)):
        left, right, max_sub = add_type(input_array, s, left, right, i, max_sub)

    print(max_sub, s)
