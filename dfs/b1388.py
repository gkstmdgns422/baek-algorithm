# 판자가 일렬로 있으면 1개로 인정되는것이 포인트이다.
# swea 쇠막대기 자르기와 유사한 방식으로 풀이

N, M = map(int, input().split())
floor = [list(input()) for _ in range(N)] # 입력값이 ----처럼 붙어있기에 인덱스 활용시 list()사용필수

cnt = 0
for u in range(N):
    for v in range(M):
        if floor[u][v] == '-': # -인 판자 확인
            cnt += 1
            if 1 <= v and floor[u][v-1] == '-': # 그전이 -판자였으면 1개 이기에 cnt -= 1
                cnt -= 1

for v in range(M):
    for u in range(N):
        if floor[u][v] == '|': # |인 판자 확인
            cnt += 1
            if 1 <= u and floor[u-1][v] == '|': # 그전이 |판자였으면 1개 이기에 cnt -= 1 
                cnt -= 1
print(cnt)