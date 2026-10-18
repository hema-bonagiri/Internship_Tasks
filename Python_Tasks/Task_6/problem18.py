# Problem 18: Set Mutations
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

a = int(input())
set_a = set(map(int,input().split()))

n = int(input())

for i in range(n):
    op = input().split()
    len = int(op[1])
    set_b = set(map(int,input().split()))
    
    if op[0] == "update":
        set_a.update(set_b)
    elif op[0] == "intersection_update":
        set_a.intersection_update(set_b)
    elif op[0] == "difference_update":
        set_a.difference_update(set_b)
    elif op[0] == "symmetric_difference_update":
        set_a.symmetric_difference_update(set_b)
    
print(sum(set_a))
    


    
