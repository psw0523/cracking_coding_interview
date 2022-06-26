'''
Problem
Asked by Google.

Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset(i,j)
satisfies either i % j = 0 or j % i = 0.

For example, given the set [3,5,10,20,21], you should return [5,10,20].
Given [1,3,6,24] return [1,3,6,24]
'''

'''
Solution

Question
- Is this array sorted?

1. If not sorted, firstly sort array.
2. Important thing is.. largest subset, that means items are consecutive,
3. The last item is largest. If N is largest index, following is true.
   If N, N-1, N-2 satisfies this condition,
  a[N] % a[N-1] = 0 and a[N-1] % a[N-2] = 0 and a[N] % a[N-2] = 0
  So we don't need to calculate between a[N] and a[N-2]
4. Start from largest index
   left, right
   cur = 0
   max = (0, 0, 0)
   for right = len(a) - 1, right >= 1, right -= 1
      cur = a[right]
     for left = right - 1, left >=0, left -= 1
       if cur % a[left] == 0:
          cur = a[left]
       else:
         save left, right, and len = right - left + 1 to max tuple (length, left, right)
         break
'''

def largest_subset(a):
    left = 0
    right = 0
    cur = 0
    max = (0, 0, 0)
    #  for right in range(len(a) - 1, -1, -1):
    right = len(a) - 1
    while right >= 1:
        cur = a[right]
        for left in range(right - 1, -1, -1):
            if cur % a[left] == 0:
                cur = a[left]
            else:
                length = right - left
                if length > max[0]:
                    max = (length, left+1, right)
                break

        if left == 0:
            break

        right = left
        if (right + 1) < max[0]: # don't need to go ahead
            break

    # check max variable is not updated
    if max[0] == 0:
        max = (right - left + 1, left, right)
    return a[max[1]:max[2]+1]



if __name__ == '__main__':
    print(largest_subset([1,3,6,24]))
    print(largest_subset([3,5,10,20,21]))

