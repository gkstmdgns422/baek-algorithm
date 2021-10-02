import sys

N, P = map(int, sys.stdin.readline().split())
lst = [set() for _ in range(7)] # 6개의 줄
cnt = 0
for _ in range(N):
    num1, num2 = map(int, sys.stdin.readline().split())
    if num2 in lst[num1]:
        cnt -= 1
    else:
        lst[num1].add(num2)
    queue = []
    while lst[num1]:
        sound = lst[num1].pop()
        if sound > num2:
            cnt += 1
        elif sound == num2:
            queue.append(sound)
            cnt += 1
        else:
            queue.append(sound)
    for i in queue:
        lst[num1].add(i)
print(cnt)
        


