import sys
sys.setrecursionlimit(100000) # 안적으면 에러뜬다.

def dfs(u,v):
    global cnt
    paper[u][v] = 1
    cnt += 1
    for i in range(4):
        y, x = u+dx[i], v+dy[i]
        if 0 <= x < N and 0 <= y < M and paper[y][x] == 0:
            dfs(y,x)
    return cnt
    

M, N, K = map(int, input().split())
paper = [[0] * N for _ in range(M)]
for _ in range(K):
    lx, by, rx, ty = map(int, input().split())
    for i in range(by,ty):
        for j in range(lx,rx):
            paper[i][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
area = []
for u in range(M):
    for v in range(N):
        if paper[u][v] == 0:
            cnt = 0
            dfs(u,v)
            area.append(cnt)

area.sort()
print(len(area))
print(*area)
