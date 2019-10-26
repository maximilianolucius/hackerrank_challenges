# Queen's Attack Challenge
#!/bin/python3

import math
import os
import random
import re
import sys
from copy import copy

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    ct = 0 # acumulator of k moves.
    # row
    osts = [o for o in obstacles if o[0] == r_q]
    tmp = c_q-1
    for o in osts:
        if o[1] < c_q:
            if tmp > c_q - o[1] - 1:
                tmp = c_q - o[1] - 1
    ct += tmp
    tmp = n-c_q
    for o in osts:
        if o[1] > c_q:
            if tmp > o[1] - c_q - 1:
                tmp = o[1] - c_q - 1
    ct += tmp
    # col
    osts = [o for o in obstacles if o[1] == c_q]
    tmp = r_q-1
    for o in osts:
        if o[0] < r_q:
            if tmp > r_q - o[0] - 1:
                tmp = r_q - o[0] - 1
    ct += tmp
    tmp = n-r_q
    for o in osts:
        if o[0] > r_q:
            if tmp > o[0] - r_q - 1:
                tmp = o[0] - r_q - 1
    ct += tmp
    # + Diagonal 
    osts = [o for o in obstacles if r_q-c_q == o[0]-o[1]]
    tmp = min(r_q-1,c_q-1)
    for o in osts:
        if o[1] < c_q:
            if tmp > c_q - o[1] - 1:
                tmp = c_q - o[1] - 1
    ct += tmp
    tmp = min(n-r_q,n-c_q)
    for o in osts:
        if o[1] > c_q:
            if tmp > o[1] - c_q - 1:
                tmp = o[1] - c_q - 1
    ct += tmp
    # - Diagonal 
    osts = [o for o in obstacles if r_q+c_q == o[0]+o[1]]
    tmp = min(n-r_q,c_q-1)
    for o in osts:
        if o[1] < c_q:
            if tmp > c_q - o[1] - 1:
                tmp = c_q - o[1] - 1
    ct += tmp
    tmp = min(r_q-1,n-c_q)
    for o in osts:
        if o[1] > c_q:
            if tmp > o[1] - c_q - 1:
                tmp = o[1] - c_q - 1
    ct += tmp

    return ct


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
