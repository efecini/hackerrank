'''Problem Link: https://www.hackerrank.com/challenges/py-set-union/problem'''
_ = input()
s1 = set(map(int, input().split()))
_ = input()
s2 = set(map(int, input().split()))

print(len(s1.union(s2)))
