def minion_game(string):
    s = {'name': 'Stuart', 'score':0}
    k = {'name': 'Kevin', 'score':0}
    vowels = {'A','E','I','O','U'}
    for i in range(len(string)):
        if string[i] in vowels: k['score'] += len(string)-i
        else: s['score'] += len(string)-i

    if s['score']>k['score'] : print(s['name'],s['score'])
    elif k['score']>s['score'] : print(k['name'],k['score'])
    else: print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)