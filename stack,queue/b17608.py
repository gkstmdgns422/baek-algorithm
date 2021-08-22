import sys

N = int(input())
stick = []
for _ in range(N):
    stick.append(int(sys.stdin.readline().rstrip()))
num = cnt = 0


for idx in range(N-1,-1,-1): # 거꾸로 계산(오른쪽에서 바라보기 때문)
    if stick[idx] > num:
        num = stick[idx]
        cnt += 1
print(cnt)

