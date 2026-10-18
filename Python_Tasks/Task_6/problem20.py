# Problem 20:Validating the Phone Number
# HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    ph_no = input()
  
    if (len(ph_no)==10 and ph_no.isdigit() and ph_no.startswith(('9','8','7'))):
        print("YES")
    else:
        print("NO") 
