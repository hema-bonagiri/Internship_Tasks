# Problem 17: Check Strict Superset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

set_A = set(map(int, input().split()))
n = int(input())
res = True

for i in range(n):
    set_B = set(map(int, input().split()))

    if not (set_A > set_B):
        res = False
        break

print(res)
