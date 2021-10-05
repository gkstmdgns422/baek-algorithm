s = [list(input()) for _ in range(9)]
stop = False


def check(i, j):
    num = ['1','2','3','4','5','6','7','8','9']
    for u in range(3*(i//3), 3*(i//3)+3): # 3*3확인
        for v in range(3*(j//3), 3*(j//3)+3):
            if s[u][v] in num:
                num.remove(s[u][v])
    for x in range(9): # 가로/세로 확인
        if s[i][x] in num:
            num.remove(s[i][x])
        if s[x][j] in num:
            num.remove(s[x][j])
    return num


def puzzle(n, v):
    global stop
    if stop:
        return

    if v == 9:
        n += 1
        v = 0

    if n == 9:
        stop = True
        for idx in range(9):
            print(''.join(s[idx]))

        return

    if s[n][v] != '0':
        puzzle(n, v + 1)
    else:
        for l in check(n,v):
            s[n][v] = l
            puzzle(n,v + 1)
        s[n][v] = '0'

puzzle(0,0)