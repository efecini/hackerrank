if __name__ == '__main__':
    lis = [[input(), float(input())] for i in range(int(input()))]
    second_best = sorted(list(set([score for name, score in lis])))[1]
    print('\n'.join([name for name, score in sorted(lis) if score == second_best]))
