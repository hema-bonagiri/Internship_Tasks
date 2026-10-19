# Problem 13: Sherlock and the Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    count = Counter(s)
    freq = Counter(count.values())

    if len(freq) == 1:
        return "YES"

    if len(freq) == 2:
        f1, f2 = sorted(freq.keys())
        if f1 == 1 and freq[f1] == 1:
            return "YES"
        if f2 - f1 == 1 and freq[f2] == 1:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    fptr.write(result + '\n')
    fptr.close()
