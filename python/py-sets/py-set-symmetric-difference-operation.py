'''Problem Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem'''

_ = input()
s1 = set(map(int, input().split()))
_ = input()
s2 = set(map(int, input().split()))

print(len(s1.symmetric_difference(s2)))