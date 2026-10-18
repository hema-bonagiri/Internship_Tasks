# Problem 14: Set .intersection() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

e = int(input())
e_no = set(map(int,input().split()))
f = int(input())
f_no = set(map(int,input().split()))

subscribed= e_no.intersection(f_no)
print(len(subscribed))
