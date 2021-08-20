T = int(input())

for tc in range(1, T+1):
    L = input().split()
    print('Case #{}: {}'.format(tc, ' '.join(L[::-1])))