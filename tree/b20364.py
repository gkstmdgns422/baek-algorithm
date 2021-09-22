# 시간초과 이유 : 홀수 숫자를 2로 나눈 몫을 구할때 시간을 많이 소비하는것 같다.
# if num%2: num -= 1 이 문장 하나의 차이로 시간초과 or 맞았습니다가 결정 났다.
import sys

N, Q = map(int, sys.stdin.readline().split())

visited = [0 for _ in range(N+1)]
for _ in range(Q):
    area = int(sys.stdin.readline())
    num = area
    found = 0
    while num > 1:
        if visited[num]:
            found = 1
            ans = num         
        if num%2:
            num -= 1
        num //= 2
    if found:
        print(ans)
    else:
        visited[area] = 1
        print(0)

# 틀렸습니다 원인 분석
# 조상을 알아보는 방식으로 진행했는데 알고보니 가야하는 땅에 가장 가까운 곳부터 찾는 코드였다.
# 따라서 코드수정을 하여 루트에서 가장 가까운 조상을 프린트하게 해야한다.
# N, Q = map(int, input().split())

# visited = [0 for _ in range(N+1)]
# for _ in range(Q):
#     area = int(input())
#     num = area
#     while num > 1:
#         if visited[num]:
#             print(num)
#             break          
#         else:
#             num //= 2
#         if num == 1:
#             visited[area] = 1
#             print(0)
#             break
