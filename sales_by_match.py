#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sorted_array = sorted(ar)
    socks_pairs = 0
    while sorted_array:
        times_of_repetition= sorted_array.count(sorted_array[0])
        if times_of_repetition % 2 == 0:
            socks_pairs += times_of_repetition / 2
        else:
            socks_pairs += (times_of_repetition - 1) / 2
        del sorted_array[: times_of_repetition]
    return int(socks_pairs)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
