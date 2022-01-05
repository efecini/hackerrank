'''Problem Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lis = []
    [lis.append(obj) for obj in arr if obj not in lis]
    lis.sort(reverse=True)
    print(lis[1])
