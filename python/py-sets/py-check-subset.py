'''Problem Link: https://www.hackerrank.com/challenges/py-check-subset/problem'''

n = input()
for i in range(int(n)):
    _ = input()
    A = set(input().split())
    _ = input()
    B = set(input().split())
    print(A.issubset(B) and len(B)>len(A))
