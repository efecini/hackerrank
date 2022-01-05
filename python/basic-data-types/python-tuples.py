'''Problem Link: https://www.hackerrank.com/challenges/python-tuples'''

if __name__ == '__main__':
    n = int(input())
    int_list = map(int, input().split())
    print(hash(tuple(x for x in int_list)))
