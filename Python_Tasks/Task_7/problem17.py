# Problem 17: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

import math
import os
import random
import re
import sys

def separateNumbers(s):
    # Write your code here
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        current = first
        result = ""

        while len(result) < len(s):
            result += str(current)
            current += 1

        if result == s:
            print("YES", first)
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)
