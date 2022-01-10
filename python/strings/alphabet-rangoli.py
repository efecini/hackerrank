import string

def print_rangoli(size):
    alpha = string.ascii_lowercase[:size][::-1]
    pattern = ['-'.join(alpha[:i+1]+alpha[:i][::-1]).center((size*4)-3,'-') for i in range(size)]
    print('\n'.join(pattern + pattern[::-1][1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)