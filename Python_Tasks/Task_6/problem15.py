# Problem 15: Set .difference() Operation
# HackerRank Link : https://www.hackerrank.com/challenges/py-set-difference-operation/problem

e = int(input())
e_no = set(map(int,input().split()))
f = int(input())
f_no = set(map(int,input().split()))

subscribed= e_no.difference(f_no)
print(len(subscribed))
