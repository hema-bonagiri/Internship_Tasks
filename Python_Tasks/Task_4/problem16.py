# Problem 16 : Nested Lists
# HackerRank Link : https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    
    unique_grades=sorted(set(student[1] for student in students))
    second_lowest = unique_grades[1]
    
    names = []
    for student in students:
        if second_lowest==student[1]:
            names.append(student[0])
    
    for i in sorted(names):
        print(i)
    
            
