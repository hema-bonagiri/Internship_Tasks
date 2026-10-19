# Problem 1: Set .symmetric_difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem


e =int(input())
e_sub = set(map(int,input().split()))
f =int(input())
f_sub = set(map(int,input().split()))

print(len(e_sub^f_sub))
