# Problem 2:The Captain's Room
# HackerRank Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import Counter
group_size = int(input())
room_no_list = map(int,input().split())

d = Counter(room_no_list)
captain_room = min(d,key=d.get)
print(captain_room)

