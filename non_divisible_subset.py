# Non-Divisible Subset
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    if len(s) == 1: return 1
    if k ==1 : return 1

    div_dict = {}
    for n in range(k):
        div_dict[n] = 0
    
    to = len(s) // 2 + 6 if len(s)/k > 10 else len(s)
    to = len(s)
    for n in range(to):
        div_dict[s[n] % k] += 1

    nondiv=1 if div_dict[0] >0 else 0 

    for m in range(1, k):
        if m == k - m:
            nondiv+=1 if div_dict[m] >0 else 0 
            break
        if m > k - m:
            break
        if div_dict[m] >= div_dict[k-m]:
            nondiv += div_dict[m]
        else:
            nondiv += div_dict[k-m]
    return nondiv

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
