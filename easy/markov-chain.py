'''
Problem
Asked by Google.

You are given a starting state start, a list of transition probalities for a Markov chain, and a number of steps num_steps.
Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities.

[
    (a, a, 0.9),
    (a, b, 0.075),
    (a, c, 0.025),
    (b, a, 0.15),
    (b, b, 0.8),
    (b, c, 0.05),
    (c, a, 0.25),
    (c, b, 0.25),
    (c, c, 0.5)
]

One instance of running this Markov chain might produce
{ a: 3012, b: 1656, c: 332 }

[3080 1571  349]
'''

'''
Solution

Transition Matrix
and Monte Carlo walking
    a      b       c
a  0.9   0.075   0.025
b  0.15  0.8     0.05
c  0.25  0.25    0.5

np.random.choice(['a','b','c'], p=A[state])
'''

import numpy as np

def montecarlo(tr_mat, start, steps):
    acc = np.array([0] * len(tr_mat[0]))
    acc[start] += 1
    prev_state = start
    n = 1

    while n < steps:
        cur_state = np.random.choice([0,1,2], p=tr_mat[prev_state])
        acc[cur_state] += 1
        prev_state = cur_state
        n += 1

    return acc/steps


def multiply(tr_mat, steps):
    n = 0
    mat = tr_mat
    while n < steps:
        mat = np.matmul(mat, tr_mat)
        n += 1

    return mat


# TODO
def find_probability(seq, tr_mat, pi):
    # seq: state sequence, ex> a -> b -> a -> c
    # tr_mat : transition matrix
    # pi: stationary probability
    start_state = seq[0]
    prob = pi[seq[start_state]]
    prev_state = start_state
    i = 1
    while i < len(seq):
        cur_state = seq[i]
        prob *= tr_mat[prev_state][cur_state]
        prev_state = cur_state
        i += 1
    return prob


if __name__ == '__main__':
    transition_matrix = np.array([[0.9, 0.075, 0.025], [0.15, 0.8, 0.05], [0.25, 0.25, 0.5]])
    pi = montecarlo(transition_matrix, 0, 5000)
    print(pi)
    #  print(multiply(transition_matrix, 5000)[0] * 5000)
    print(find_probability([0, 1, 0, 2], transition_matrix, pi))
    print(find_probability([0, 1, 1, 0], transition_matrix, pi))
