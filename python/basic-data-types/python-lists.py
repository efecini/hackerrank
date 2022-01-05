'''Porblem List: https://www.hackerrank.com/challenges/python-lists/'''

if __name__ == '__main__':
    lis = []
    for _ in range(int(input())):
        cmd_args = input().split()
        cmd = cmd_args[0]
        args = cmd_args[1:]
        if cmd == 'print':
            print(lis)
        else:
            cmd += "(" + ",".join(args) + ")"
            eval("lis."+cmd)
