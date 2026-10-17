# Problem 7 : Symmetric Difference
# HackerRank Link : https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
set1 = set(map(int,input().split()))
n = int(input())
set2= set(map(int,input().split()))

symmetric_diff = set1.symmetric_difference(set2)
for i in sorted(symmetric_diff):
    print(i)
