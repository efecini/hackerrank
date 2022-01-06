"Problem Link: https://www.hackerrank.com/challenges/list-comprehensions/problem?"

if __name__ == '__main__':
    x,y,z,n = (int(input()) for _ in range(4))
    print([[a,b,c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c != n])

scores = [-100, -100]
for _ in range(int(input())):
    i = int(input())
    if i < scores[i]:
        continue
    elif i <= scores[0]:
        scores[1] = i
    else:
        scores[0] = i
print(scores[0])