'''Problem Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true'''

n = int(input())
A = set(input().split())
B = set()

for _ in range(n):
    B = B.union(set(input().split()))

print(A.issuperset(B))
