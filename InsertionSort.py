#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
   
    val=arr[n-1]
    for j in range(n-1, -1, -1):
        if arr[j-1] >val  and j!=0:
            arr[j]=arr[j-1]
            print(*arr)
        else:
             arr[j] = val
             print(*arr)
             break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
