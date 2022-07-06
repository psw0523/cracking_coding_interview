'''
Problem
Asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is "abcde" and B is "cdeab", return true.
If A is abc and B is acb, return false
'''

'''
Solution

1. check length is same
2. find position of a[0] on b
               abcde
               cdeab
                  found i
                  offset = i
               b[i]
3. If found, while i < len(a), a[i] == b[(start+i) % length]
'''

def a_shifted_to_b(a, b):
    if len(a) != len(b):
        return False

    b_i = 0
    for i in range(len(a)):
        if b[i] == a[0]:
            b_i = i
            break

    i = 1
    while i < len(a) and a[i] == b[(b_i + i) % len(a)]:
        i += 1

    if i == len(a):
        return True

    return False


if __name__ == '__main__':
    print(a_shifted_to_b("abcde", "cdeab"))
    print(a_shifted_to_b("abc", "acb"))

