# Problem 6: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem

import math
import os
import random
import re
import sys

def pangrams(s):
    # Write your code here
     s= s.lower()
     unique_chars = set(char for char in s if char.isalpha())
     if len(unique_chars)==26:
        return "pangram"
     return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = pangrams(s)
    fptr.write(result + '\n')
    fptr.close()
