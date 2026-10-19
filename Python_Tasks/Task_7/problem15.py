# Problem 15: Game of Thrones - I
# HackerRank Link: https://www.hackerrank.com/challenges/game-of-thrones/problem

import math
import os
import random
import re
import sys
from collections import Counter

def gameOfThrones(s):
    # Write your code here
    count = Counter(s)
    odd = 0

    for value in count.values():
        if value % 2 != 0:
            odd += 1

    if odd <= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = gameOfThrones(s)
    fptr.write(result + '\n')
    fptr.close()
