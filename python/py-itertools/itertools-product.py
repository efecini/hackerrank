'''Problem Link: https://www.hackerrank.com/challenges/itertools-product/problem'''
from itertools import product

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

print(*product(l1, l2))
