N, K = map(int,input().split())
money_type = []
for i in range(N):
    money_type.append(int(input())) # 돈 종류별 리스트 저장
cnt = 0
while True:
    if not K:
        break
    cnt += K // money_type[N-1] # 오름차순으로 정렬되있기에 N-1인덱스부터 시작
    K = K % money_type[N-1]
    N -= 1
print(cnt)