import sys
sys.setrecursionlimit(100000)

N = int(input())
citys = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N

ans = 0
min_num = 10**8
def dfs(v, cnt):
    global ans, min_num
    if cnt == N and citys[v][0] > 0: # 한바퀴 순회 가능한가? ( 시작지점이 0부터 시작하였으니 돌아오는것(v->0)도 존재해야함)
        min_num = min(min_num, ans + citys[v][0])
        return min_num


    for i in range(N):
        if citys[v][i] and not visited[i]:
            visited[i] = 1
            ans += citys[v][i]
            dfs(i, cnt+1)
            visited[i] = 0
            ans -= citys[v][i]

visited[0] = 1 # 처음은 추가 (돌아올때 계산 해야하므로 빼야함)
dfs(0,1) # cnt가 1번부터 시작하는 이유 : 돌아오는걸 따로 계산할것이기 때문에

print(min_num)