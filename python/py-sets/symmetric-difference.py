'''Problem Link: https://www.hackerrank.com/challenges/symmetric-difference'''
m = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))

[print(n) for n in sorted(s1.union(s2)-s1.intersection(s2))]
