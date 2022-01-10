'''Problem Link: https://www.hackerrank.com/challenges/text-wrap/problem'''
import textwrap

def wrap(s, w):
    return "\n".join(textwrap.wrap(s,w))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)