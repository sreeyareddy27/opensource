import math
import os
import random
import re
import sys
def plusMinus(arr):
    n=0
    p=0
    z=0
    for i in arr:
        if i<0:
            n+=1
        elif i>0:
            p+=1
        elif i==0:
            z+=1
    print(p/len(arr))
    print(n/len(arr))
    print(z/len(arr))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
