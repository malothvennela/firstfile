import math
import os
import random
import re
import sys
def reverseArray(a):
    # Write your code here
    z=[]
    for i in range(len(a)-1,-1,-1):
        z.append(a[i])
    return z
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
