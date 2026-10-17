# Problem 20 : Piling Up!
# HackerRank Link : https://www.hackerrank.com/challenges/piling-up/problem

t = int(input())

for _ in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))

    i = 0
    j = n - 1
    last = float('inf')
    possible = True

    while i <= j:
        if blocks[i] >= blocks[j]:
            current = blocks[i]
            i += 1
        else:
            current = blocks[j]
            j -= 1

        if current > last:
            possible = False
            break

        last = current

    if possible:
        print("Yes")
    else:
        print("No")
