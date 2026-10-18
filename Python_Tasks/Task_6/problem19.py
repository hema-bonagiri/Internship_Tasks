# Problem 19: Company Logo
# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()

    d = Counter(s)
    for char, freq in sorted(d.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(char, freq)
