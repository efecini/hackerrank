'''https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true'''

_ = int(input())
s = set(input().split())

for _ in range(int(input())):
    eval('s.{0}({1})'.format(input().split()[0],input().split()))
print(sum([int(i) for i in s]))
