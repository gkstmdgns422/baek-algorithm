# 배열은 크기 순서대로 가운데를 체워가야 최소의 난이도가 나온다. 
# 예시 : [1,2,3,4,5] => [1,3,5,4,2] or [5,3,1,2,4]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    log = list(map(int,input().split())) 
    log.sort()
    max_val = 0
    for i in range(N-2): # 양옆의 차의 최대값은 인덱스가 2가 차이난다.
        if max_val < abs(log[i]-log[i+2]):
            max_val = abs(log[i]-log[i+2])
    print(max_val)
    