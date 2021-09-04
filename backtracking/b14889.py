import sys
sys.setrecursionlimit(100000)

def dfs(start,cnt):
    global min_num
    if cnt == N//2:
        a, b = 0, 0
        for i in range(N):
            for j in range(i,N):
                if visited[i] and visited[j]:
                    a += team[i][j] + team[j][i]
                elif not visited[i] and not visited[j]:
                    b += team[i][j] + team[j][i]
        min_num = min(min_num,abs(a-b)) 
        return
    for i in range(start,N):
        if not visited[start]:
            visited[i] = 1
            dfs(i+1,cnt+1)
            visited[i] = 0

N = int(input())
team = [list(map(int,input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
min_num = 100000


dfs(0,0)
print(min_num)

