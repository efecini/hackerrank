'''Problem Link: https://www.hackerrank.com/challenges/string-validators
'''

if __name__ == '__main__':
    s = input()

    print(f"{any(x.isalnum() for x in s)}")
    print(f"{any(x.isalpha() for x in s)}")
    print(f"{any(x.isdigit() for x in s)}")
    print(f"{any(x.islower() for x in s)}")
    print(f"{any(x.isupper() for x in s)}")