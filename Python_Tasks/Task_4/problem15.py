# Problem 15.py
# HackerRank Link : https://www.hackerrank.com/challenges/word-order/problem

n = int(input())
words = {}

for word in range(n):
    word = input()
    words[word] = words.get(word,0)+1

print(len(words))
print(*words.values())    
