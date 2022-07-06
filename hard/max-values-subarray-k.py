'''
Problem
Aaked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array,
Compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
we should get: [10,7,8,8], since:
    - 10 = max(10,5,2)
    - 7 = max(5,2,7)
    - 8 = max(2,7,8)
    - 8 = max(7,8,7)

Do this in O(n) time and O(k) space.
You can modify the input array in place and you do not need to store the results.
You can simply print them out as you compute them.
'''

'''
Solution

a = [10,5,5,7,8,7]

Go to index 2.
max_value = max(a[0], a[1])
if a[2] < a[1]:
    a[2] = a[1]
else:
    max_value = max(max_value, a[2])

print(max_value)

prev = a[2]

i = 3; i < len(input); i++
if a[i] > prev:
    print(a[i])
else:
    a[i] = prev
    print(prev)
'''

def print_max_value_of_k(a, k):
    max_value = max(a[0], a[1])
    i = 1
    while i < (k - 1):
        if a[i+1] < a[i]:
            a[i+1] = a[i]
        else:
            max_value = max(max_value, a[i+1])
        i += 1

    print(max_value)

    prev = a[k-1]
    i = k
    while i < len(a):
        if a[i] > prev:
            print(a[i])
            prev = a[i]
        else:
            a[i] = prev
            print(prev)
        i += 1
  

if __name__ == '__main__':
    print_max_value_of_k([10,5,5,7,8,7], 3)
    print("")
    print_max_value_of_k([10,5,5,7,8,7], 4)
    print("")
    print_max_value_of_k([10,5,5,7,8,7], 5)
    print("")
    print_max_value_of_k([10,5,5,7,8,7], 6)
