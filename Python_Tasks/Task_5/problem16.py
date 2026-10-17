# Problem 16 : Collections.Counter()
# HackerRank Link : https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

no_of_shoes = int(input())
sizes = Counter(map(int,input().split()))
no_of_cust = int(input())
money_earned = 0

for i in range(no_of_cust):
    size,price = map(int,input().split())
    
    if sizes[size]>0:
        money_earned+=price
        sizes[size]-=1
print(money_earned)

