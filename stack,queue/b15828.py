N = int(input()) # 버퍼의 크기
queue = []
while True:
    p = input()
    if p == '-1': # 종료문
        break
    elif p == '0': # 처리
        queue.pop(0)
    elif len(queue) < N:
        queue.append(p)
if queue:
    print(*queue)
else:
    print('empty')


