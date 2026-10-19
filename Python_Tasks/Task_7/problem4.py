# Problem 4: Funny String
# HackerRank Link: https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    s = list(s)
    r = s[::-1]

    a = []
    for i in s:
        a.append(ord(i))

    b = []
    for i in r:
        b.append(ord(i))

    funny = True

    for i in range(len(a) - 1):
        if abs(a[i+1] - a[i]) != abs(b[i+1] - b[i]):
            funny = False
            break

    if funny:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
