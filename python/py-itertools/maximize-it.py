'''Problem Link: https://www.hackerrank.com/challenges/maximize-it/problem'''

from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
print(max(map(lambda x: sum(i**2 for i in x)%M, product(*N))))
