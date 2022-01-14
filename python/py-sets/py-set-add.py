'''Problem Link: https://www.hackerrank.com/challenges/py-set-add/problem'''

s = set()
n = input()
[s.add(input()) for _ in range(int(n))]
print(len(s))
