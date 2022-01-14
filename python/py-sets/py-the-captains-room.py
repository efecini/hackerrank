'''Problem Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true'''

k = int(input())
l = list(map(int, input().split()))
sum_l = sum(l)
sum_s = sum(set(l)) * k

print((sum_s - sum_l) // (k - 1))