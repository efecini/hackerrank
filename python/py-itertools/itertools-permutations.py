'''Problem Link: https://www.hackerrank.com/challenges/itertools-permutations/problem'''

from itertools import permutations
s, n = input().split()
l1 = [''.join(i) for i in permutations(sorted(s),int(n))]
print(*l1,sep='\n')
