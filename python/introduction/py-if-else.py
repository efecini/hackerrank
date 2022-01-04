'''Problem Link: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true'''

if __name__ == '__main__':
    n = int(input().strip())

    if n%2 or n in range(6, 21):
        print('Weird')
    else:
        print('Not Weird')