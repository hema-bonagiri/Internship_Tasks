#Problem 9: Mutations
#HackerRank Link: https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    
   lis = list(string)
   lis[position]=character
   modified_string = "".join(lis)
   return modified_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
