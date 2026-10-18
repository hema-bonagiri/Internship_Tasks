# Problem 13: Set .union() Operation
# HackerRank Link : https://www.hackerrank.com/challenges/py-set-union/problem

e = int(input())
e_no = set(map(int,input().split()))
f = int(input())
f_no = set(map(int,input().split()))

subscribed= e_no.union(f_no)
print(len(subscribed))
