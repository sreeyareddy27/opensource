import math
import os
import random
import re
import sys
def missingNumbers(arr, brr):
    a={}
    b={}
    for num in arr:
        a[num]=a.get(num,0)+1
    for num in brr:
        b[num]=b.get(num,0)+1
    m=[]
    for num,freq in b.items():
        if num not in a or a[num]<freq:
            m.append(num)
    return sorted(set(m))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
