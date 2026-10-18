# Problem 20:Validating the Phone Number
# HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(input())
for i in range(n):
    phone = input()

    if re.fullmatch(r'[789]\d{9}', phone):
        print("YES")
    else:
        print("NO")

