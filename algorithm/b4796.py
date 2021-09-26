tc = 1
while True:
    L, P, V = map(int, input().split())
    cnt = 0
    if L or P or V:
        cnt = V//P * L
        if V%P < L:
            cnt += V%P
        else:
            cnt += L
        print('Case {}: {}'.format(tc, cnt))
        tc += 1
    else:
        break