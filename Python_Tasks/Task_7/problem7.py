# Problem 7: Alphabet Rangoli
# HackerRank Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string
def print_rangoli(size):
    chars = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    for i in range(size):
        left = [chars[j] for j in range(size - 1, i - 1, -1)]
        row = left + left[:-1][::-1]
        line = "-".join(row)
        lines.append(line.center(width, "-"))

    print("\n".join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
