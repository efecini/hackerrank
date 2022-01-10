'''Problem Link: https://www.hackerrank.com/challenges/merge-the-tools/problem
'''

def merge_the_tools(string, k):
    for i in range(len(string)//k):
        s = (string[(i*k):k*(i+1)])
        print(''.join(sorted(set(s),key=s.index)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)