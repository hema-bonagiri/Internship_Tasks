# Problem 8 : Set .add()
# HackerRank Link : https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
country = set()

for i in range(n):
    country.add(input())
print(len(country))
