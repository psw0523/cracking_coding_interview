'''
Problem
Asked by Google.

Given an interger n and a list of integers l,
write a function that randomly generates a number from 0 to n - 1
that isn't in l(uniform).
'''

'''
Solution

Question
- What is the meaning of uniform?
- Generation number is integer or 실수? Maybe integer
- Can I use python random module?

If I can use python random module, solution is very easy.

import random as rand

number = rand.randrange(0, N)
if number not in num_lists:
    return number
'''

import random as rand

def random_gen(num_lists, n):
    found = False
    num = None
    while found is False:
        num = rand.randrange(0, n)
        if num not in num_lists:
            found = True
    return num


if __name__ == '__main__':
    num_lists = [1, 3, 5]
    for i in range(10):
        print(random_gen(num_lists, 10))

