if __name__ == '__main__':
    s = input()
    #Use any. This is a good use case.
    print(f"{any(x.isalnum() for x in s)}")
    print(f"{any(x.isalpha() for x in s)}")
    print(f"{any(x.isdigit() for x in s)}")
    print(f"{any(x.islower() for x in s)}")
    print(f"{any(x.isupper() for x in s)}")